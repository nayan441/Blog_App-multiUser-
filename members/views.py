from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib.auth import authenticate,login,logout
from multiuser import settings
from django.contrib.auth.views import PasswordChangeView
# Create your views here.
from django.contrib.auth.views import LoginView   
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

class LoginView(SuccessMessageMixin,LoginView):
    template_name = 'registration/login.html'
    success_url=reverse_lazy('home')
    success_message = "You were successfully logged in"



class PasswordChangeView(PasswordChangeView):
    form_class=PasswordChangeForm
    success_message = "User password changed successfully"
    success_url=reverse_lazy('home')



class UserRegistrationView(CreateView):
    form_class=CustomUserCreationForm    
    success_url=reverse_lazy('login')
    success_message = "User registered successfully"
    template_name='registration/registration.html'
# class UserRegistrationView(CreateView):
#     form_class=UserCreationForm    
#     success_url=reverse_lazy('login')
#     template_name='registration/registration.html'


class UserEditView(UpdateView):
    form_class=CustomUserChangeForm    
    success_url=reverse_lazy('home')
    template_name='registration/edit_profile.html'
    success_message = "User edited successfully"

    def get_object(self):
        return self.request.user


# class LoginView(View):
#     def post(self, request):  ``
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)

#         if user is not None:
#             if user.is_active:
#                 login(request, user)

#                 return HttpResponseRedirect('home')
#             else:
#                 return HttpResponse("Inactive user.")
#         else:
#             return HttpResponseRedirect(settings.LOGIN_URL)

#         return render(request, "home.html")

class LogoutView(SuccessMessageMixin,View):
    
    def get(self, request):
        logout(request)
        messages.success(request,'You were successfully logout')
        return render(request, 'registration/logout.html')
        # return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)

