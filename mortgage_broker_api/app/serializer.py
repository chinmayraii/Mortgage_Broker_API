from rest_framework import serializers
from . models import Chatbot,Ticket,Message
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            password=validated_data['password']
        )
        return user

# class UserLoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()

#     def validate(self, attrs):
#         user = authenticate(username=attrs['username'], password=attrs['password'])
#         if not user:
#             raise serializers.ValidationError('Invalid username or password')
#         return attrs

class ChatbotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chatbot
        fields = ['user_details','user_input','bot_response']


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'        

class UserMessageSerializer(serializers.ModelSerializer):
    ticket_subject = serializers.CharField(source='ticket.subject')
    status = serializers.CharField(source='get_status_display')


    class Meta:
        model = Message
        fields = ['ticket','ticket_subject', 'status', 'content', 'created_at'] 
        read_only_fields = ['id', 'ticket']

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance

