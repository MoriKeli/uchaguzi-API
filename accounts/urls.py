from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='user_login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('voter-registration/', views.VoterRegistrationView.as_view(), name='voter_registration'),

]