from django.urls import path
from . import views

app_name = 'Main'
urlpatterns = [
    path('', views.landing, name="landing"),
    path('signup/', views.signup),
    path('user_dashbord', views.user_dashbord, name="user_dashbord"),
    path('feedback', views.feedback, name="feedback"),
    path('contact_us', views.contact_us, name="contact_us"),
    path('faq', views.faq, name="faq"),
    path('invoice', views.invoice, name="invoice"),

]
