from django.contrib import admin
from . models import Chatbot,CustomUser, Message, Ticket

admin.site.register(Chatbot)
admin.site.register(CustomUser)
admin.site.register(Message)
admin.site.register(Ticket)