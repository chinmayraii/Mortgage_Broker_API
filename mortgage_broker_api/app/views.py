from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Chatbot,Ticket,Message
from .serializer import UserRegistrationSerializer,ChatbotSerializer,TicketSerializer,MessageSerializer,UserMessageSerializer
from django.contrib.auth.models import User
from rest_framework import status
from .langchains import generate_response, OpenAIFunction
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import get_user_model
import uuid
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render,redirect,get_object_or_404
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from .permissions import IsTicketOwner
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
# from .conversation import save_conversation
import openai


User = get_user_model()


class UserRegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User successfully registered'}, status=201)
        return Response(serializer.errors, status=400)
    

# class UserLoginAPIView(APIView):
#     def post(self, request):
#         serializer = UserLoginSerializer(data=request.data)
#         if serializer.is_valid():
#             username = serializer.validated_data['username']
#             password = serializer.validated_data['password']
#             user = authenticate(username=username, password=password)
#             if user:
#                 login(request, user)
#                 return Response({'message': 'Login successful'})
#             else:
#                 return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


class ChatAPI(APIView):
    
        # permission_classes = [IsAuthenticated]

        def get(self, request):
            user = request.user.id
            chat_data = Chatbot.objects.filter(user_details=user)
            serializer = ChatbotSerializer(chat_data, many=True)
            return Response(serializer.data) 

        def post(self, request):
            try:
                user_input = request.data.get('message')
                user = request.user.id
                
                response=generate_response(user_input)
                message=Chatbot.objects.create(user_details=user,user_input=user_input,bot_response=response)
                message.save()
                # save_conversation(user_id,user_input,response)
                serializer = ChatbotSerializer(message)
                return Response(serializer.data)
            except:
                prompt = f"You are  <expert mortgage advisor>,<mortgage advisor for specific company> <inteligent> human current question:{user_input}\n  Now if human current question: {user_input} for something then ask human for that otherwise give best answer as a mortgage advisor "
                response = OpenAIFunction(prompt)
                message=Chatbot.objects.create(user_details=user,user_input=user_input,bot_response=response)
                message.save()
                # save_conversation(user_id,user_input,response)
                serializer = ChatbotSerializer(message)
                return Response(serializer.data)
                
            # except Exception as e:
            #     print(e)
            #     return Response(status=status.HTTP_400_BAD_REQUEST)

        # def put(self, request):
        #     request.session['user_id'] = str(uuid.uuid4())  # Generate a new user ID
        #     return Response({'message': 'User changed successfully'}, status=200) 

        def delete(self, request,user_id):
            Chatbot.objects.filter(user_id=user_id).delete()
            return Response({'message': 'User data deleted successfully'}, status=204)  



class TicketListAPIView(APIView):

    # authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    permission_classes = [IsTicketOwner]

    def get(self, request):
        tickets = Ticket.objects.filter(client=request.user)
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data.copy()
        data['client'] = request.user.id 
        serializer = TicketSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

class TicketDetailAPIView(APIView):

    permission_classes = [IsAuthenticated]
    # authentication_classes = [SessionAuthentication]
    permission_classes = [IsTicketOwner]

    def get_object(self, ticket_id):
        try:
            return Ticket.objects.get(id=ticket_id, client=self.request.user)
        except :
            return None

    def get(self, request, ticket_id=None):
        if ticket_id is not None:
            ticket = self.get_object(ticket_id)
            serializer = TicketSerializer(ticket)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        tickets = Ticket.objects.filter(client=request.user)
        serializer = TicketSerializer(tickets, many=True)
        return Response( status=status.HTTP_200_OK)

    def put(self, request, ticket_id):
        data = request.data.copy()
        data['client'] = request.user.id 
        ticket = Ticket.objects.get(id=ticket_id, client=request.user)
        serializer = TicketSerializer(ticket, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, ticket_id):
        ticket = Ticket.objects.get(id=ticket_id, client=request.user)
        ticket.delete()
        return Response(data='ticket Deleted Successfully !!!',status=status.HTTP_204_NO_CONTENT)



class MessageListAPIView(APIView):
    # def get(self, request):
    #     messages = Message.objects.all()
    #     serializer = MessageSerializer(messages, many=True)
    #     return Response(serializer.data)

    def get(self, request):
        tickets = Ticket.objects.all()
        ticket_serializer = TicketSerializer(tickets, many=True)

        messages = Message.objects.filter(ticket__in=tickets)
        message_serializer = UserMessageSerializer(messages, many=True)

        return Response({
            'tickets': ticket_serializer.data,
            'messages': message_serializer.data,
        }, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MessageDetailAPIView(APIView):
   

    def get(self, request, ticket_id):
        try:
            ticket = Ticket.objects.get(id=ticket_id)
        except Ticket.DoesNotExist:
            return Response({'detail': 'Ticket not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        ticket_serializer = TicketSerializer(ticket)
        messages = Message.objects.filter(ticket=ticket)
        message_serializer = UserMessageSerializer(messages, many=True)
        
        return Response({
            'ticket': ticket_serializer.data,
            'messages': message_serializer.data,
        }, status=status.HTTP_200_OK)
    
    def post(self, request, ticket_id):
        ticket = get_object_or_404(Ticket, id=ticket_id)
        serializer = MessageSerializer(data=request.data)

        if serializer.is_valid():
            message = serializer.save(ticket=ticket)

            # Send email notification to the ticket client
            email = ticket.client.email
            recipient_list = [email]
            subject = f"New Message - Ticket #{ticket.id}"
            email_from = settings.EMAIL_HOST_USER

            message_body = f"Hello,\n\nYou have received a new message from the Mortgage Advisor regarding Ticket #{ticket.id}.\n\nMessage: {message.content}\n\nStatus: {message.status}\n\nPlease log in to your account to view the details.\n\nBest regards,\nThe Advisor Team"

            send_mail(subject, message_body, email_from, recipient_list, fail_silently=True) 

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, ticket_id):
        try:
            message = Message.objects.get(id=ticket_id)
        except Message.DoesNotExist:
            return Response({'detail': 'Message not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserMessageSerializer(message, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, ticket_id):
        try:
            ticket = Message.objects.get(id=ticket_id)
            ticket.delete()
            return Response({'message': 'Message deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except Message.DoesNotExist:
            return Response({'error': 'Message not found.'}, status=status.HTTP_404_NOT_FOUND)


class UserDetailView(APIView):

    permission_classes = [IsAuthenticated,IsTicketOwner]

    def get(self, request):
        tickets = Ticket.objects.filter(client=request.user)
        ticket_serializer = TicketSerializer(tickets, many=True)

        messages = Message.objects.filter(ticket__in=tickets)
        message_serializer = UserMessageSerializer(messages, many=True)

        return Response({
            'tickets': ticket_serializer.data,
            'messages': message_serializer.data,
        }, status=status.HTTP_200_OK)
