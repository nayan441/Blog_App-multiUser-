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


class PasswordChangeView(PasswordChangeView):
    form_class=PasswordChangeForm
    success_url=reverse_lazy('home')



class UserRegistrationView(CreateView):
    form_class=CustomUserCreationForm    
    success_url=reverse_lazy('login')
    template_name='registration/registration.html'
# class UserRegistrationView(CreateView):
#     form_class=UserCreationForm    
#     success_url=reverse_lazy('login')
#     template_name='registration/registration.html'


class UserEditView(UpdateView):
    form_class=CustomUserChangeForm    
    success_url=reverse_lazy('home')
    template_name='registration/edit_profile.html'

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

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)
