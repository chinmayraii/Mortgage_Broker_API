from rest_framework import serializers
from . models import *
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
        fields = ['id','user_details','user_input','bot_response']


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
    

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model= Property
        fields =['property']

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']       

class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields = ['type']        

class SituationSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = SituationSearch
        fields = ['search']        

class SituationExistingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SituationExisting
        fields = ['existing']        

class CurrentCircumstancesSerializer(serializers.ModelSerializer):
    property = serializers.PrimaryKeyRelatedField(queryset=Property.objects.all())  # Use PrimaryKeyRelatedField for dropdown
    property_data = PropertySerializer(source='property', read_only=True)

    location_country = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all())  # Use PrimaryKeyRelatedField for dropdown
    country_data = CountrySerializer(source='location_country', read_only=True)

    property_type = serializers.PrimaryKeyRelatedField(queryset=PropertyType.objects.all())  # Use PrimaryKeyRelatedField for dropdown
    property_type_data = PropertyTypeSerializer(source='PropertyType', read_only=True)

    situation_regarding_search = serializers.PrimaryKeyRelatedField(queryset=SituationSearch.objects.all())  # Use PrimaryKeyRelatedField for dropdown
    situation_search_data = SituationSearchSerializer(source='situation_regarding_search', read_only=True)

    situation_regarding_existing = serializers.PrimaryKeyRelatedField(queryset=SituationExisting.objects.all())  # Use PrimaryKeyRelatedField for dropdown
    situation_existing_data = SituationExistingSerializer(source='situation_regarding_existing', read_only=True)

    class Meta:
        model = CurrentCircumstances
        fields = '__all__'      

class SourceOfFundsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceOfFunds
        fields = ['source_of_funds']       

class MortgageRequirementsSerializer(serializers.ModelSerializer):
    source = serializers.PrimaryKeyRelatedField(queryset=SourceOfFunds.objects.all())  # Use PrimaryKeyRelatedField for dropdown
    source_data = SourceOfFundsSerializer(source='source', read_only=True)

    class Meta:
        model = MortgageRequirements
        fields = '__all__'  

       

class AppsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apps
        fields = ['apps']       

class ApplicantSerializer(serializers.ModelSerializer):
    apps = serializers.PrimaryKeyRelatedField(queryset=Apps.objects.all())  # Use PrimaryKeyRelatedField for dropdown
    apps_data = AppsSerializer(source='apps', read_only=True)
    class Meta:
        model = Applicant
        fields = '__all__'        

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['status']       

class EmploymentSerializer(serializers.ModelSerializer):
    status = serializers.PrimaryKeyRelatedField(queryset=Status.objects.all())  # Use PrimaryKeyRelatedField for dropdown
    status_data = StatusSerializer(source='status', read_only=True)
    class Meta:
        model = Employment
        fields = '__all__'  

class LoansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loans
        fields = '__all__'   

class AdditionalAssistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalAssistance
        fields = ['assistance']  

class AssetsSerializer(serializers.ModelSerializer):
    assistance = serializers.PrimaryKeyRelatedField(queryset=AdditionalAssistance.objects.all())  # Use PrimaryKeyRelatedField for dropdown
    assistance_data = AdditionalAssistanceSerializer(source='assistance', read_only=True)
    class Meta:
        model = Assets
        fields = '__all__'   

class AdditionalApplicnatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalApplicnats
        fields = '__all__'   



