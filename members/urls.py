

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('register/',views.UserRegistrationView.as_view(),name='registration'),
    path('edit_profile/',views.UserEditView.as_view(),name='edit_profile'),
    path('password/',auth_views.PasswordChangeView.as_view(template_name='registration/chanmge-password.html'),name='password_change'),
    path('login/',views.LoginView.as_view(),name='login'),
    
]