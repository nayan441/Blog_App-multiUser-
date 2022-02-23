
from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  ,UserChangeForm
from django.core.exceptions import ValidationError  
# from django.forms.fields import EmailField  
# from django.forms.forms import Form  
  
class CustomUserCreationForm(UserCreationForm):  
    username = forms.CharField(label='username', min_length=5, max_length=150, widget=forms.TextInput(attrs={'class':'form-control',}))  
    first_name = forms.CharField(label='First Name', max_length=150,widget=forms.TextInput(attrs={'class':'form-control',}))  
    last_name = forms.CharField(label='Last Name', max_length=150,  widget=forms.TextInput(attrs={'class':'form-control',})) 
    email = forms.EmailField(label='email',widget=forms.EmailInput(attrs={'class':'form-control',}))  
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class':'form-control',}))  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class':'form-control',}))  
    class Meta:
        model=User
        fields = ['first_name', 'last_name', 'email', 'username','password1','password2']
    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return username  
  
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        if email[-10:]=='@gmail.com':
            new = User.objects.filter(email=email) 
        else:
             raise ValidationError(" Please provide Gmail Account-------------------------------------------------------------------------------------")   
        if new.count():  
            raise ValidationError(" Email Already Exist")  
        if email[-10:]=='@gmail.com':
            return email
        else:
            raise ValidationError(" Please provide Gmail Account-------------------------------------------------------------------------------------")   
  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match")  
        return password2  
  
    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            email=self.cleaned_data['email'],  
            password=self.cleaned_data['password1'] , 
            first_name=self.cleaned_data['first_name']  ,
            last_name=self.cleaned_data['last_name']  ,
        )  
        return user  

class CustomUserChangeForm(UserChangeForm): 
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'email', 'username',]
    username = forms.CharField(label='username', min_length=5, max_length=150, widget=forms.TextInput(attrs={'class':'form-control',}))  
    first_name = forms.CharField(label='First Name', max_length=150,widget=forms.TextInput(attrs={'class':'form-control',}))  
    last_name = forms.CharField(label='Last Name', max_length=150, widget=forms.TextInput(attrs={'class':'form-control',})) 
    email = forms.EmailField(label='email',widget=forms.EmailInput(attrs={'class':'form-control',}))  