from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('api/register/', views.UserRegistrationAPIView.as_view(), name='user-registration'),
    # path('api/login/', views.UserLoginAPIView.as_view(), name='user-login'),
    path('api/chat/', views.ChatAPI.as_view(), name='chat-ap'),
    # path('api/chat/<str:user_id>/', api.ChatAPI.as_view(), name='user_data_api'),
    # path('api/view/', views.ViweAllData.as_view(), name='view'),

    path('api/tickets/', views.TicketListAPIView.as_view(), name='ticket-list'),
    path('api/tickets/<int:ticket_id>/', views.TicketDetailAPIView.as_view(), name='ticket-detail'),
    path('api/messages/', views.MessageListAPIView.as_view(), name='message-list'),
    path('api/messages/<int:ticket_id>/', views.MessageDetailAPIView.as_view(), name='message-detail'),
    path('api/details/', views.UserDetailView.as_view(), name='user-detail'),




    

]
