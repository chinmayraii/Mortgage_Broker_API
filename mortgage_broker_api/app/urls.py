from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from app.views import GoogleLoginAPIView


urlpatterns = [
    path('api/register/', views.UserRegistrationAPIView.as_view(), name='user-registration'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/chat/', views.ChatListAPI.as_view(), name='chat-ap'),
    path('api/chat/<int:chat_id>/', views.ChatDetailAPI.as_view(), name='chat_data_api'),
    path('api/tickets/', views.TicketListAPIView.as_view(), name='ticket-list'),
    path('api/tickets/<int:ticket_id>/', views.TicketDetailAPIView.as_view(), name='ticket-detail'),
    path('api/messages/', views.MessageListAPIView.as_view(), name='message-list'),
    path('api/messages/<int:ticket_id>/', views.MessageDetailAPIView.as_view(), name='message-detail'),
    path('api/details/', views.UserDetailView.as_view(), name='user-detail'),

    path('google/login/', GoogleLoginAPIView.as_view(), name='google-login'),





    

]
