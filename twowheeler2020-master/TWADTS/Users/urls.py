from django.urls import path
from . import views

app_name = 'Users'
urlpatterns = [
    path('', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout' ),
    path('lockscreen', views.lockscreen, name='lockscreen'),
    path('forget_password', views.forget_password, name='forget_password'),

    #user Profiles
    path('personal_information',views.personal_information, name='personal_information'),
    path('bike_information',views.bike_information, name='bike_information'),
    path('emergency_contact',views.emergency_contact, name='emergency_contact'),
    path('account_information',views.account_information, name='account_information'),
    path('change_password',views.change_password, name='change_password'),
    path('email_setting',views.email_setting, name='email_setting'),

]
