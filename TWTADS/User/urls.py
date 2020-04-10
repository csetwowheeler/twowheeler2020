from django.contrib import admin
from django.urls import path
from .views import home_view, signup_view, activation_sent_view, activate,login

urlpatterns = [
    path('home/', home_view, name="home"),
    path('signup/', signup_view, name="signup"),
    path('login/',login, name='login'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
]


