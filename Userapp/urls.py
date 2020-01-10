from django.urls import path
from Userapp import views

urlpatterns=[
    path('user_dashboard/',views.userdashboard),
    path('user_reg/',views.userregister),
    path('user_login/',views.userlogin),
    path('user_welcome/',views.welcome_user),
    path('it_show_user/',views.it_showuser),
    path('mech_show_user/',views.mech_showuser),
    path('civil_show_user/',views.civil_showuser),
   
]