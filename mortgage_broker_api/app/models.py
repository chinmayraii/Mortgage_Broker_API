from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser,Group
from django.conf import settings
from django.utils import timezone


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Chatbot(models.Model):
    user_details = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    user_input = models.TextField()
    bot_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_details.username +" "+self.user_input +" "+self.bot_response
    

class Ticket(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.client.username+" "+self.subject
    
    

STATUS_CHOICES = (
    ('Enquiry', 'Enquiry'),
    ('Application', 'In Application'),
    ('Completion stage', 'Completion stage'),
)    

class Message(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

