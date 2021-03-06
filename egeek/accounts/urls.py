from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('signup_apply/', views.signup_apply, name="signup_apply"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('username_chk/', views.username_chk, name="username_chk"),
] 