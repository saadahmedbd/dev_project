from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . models import Record

from django import forms 

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

# register/create  a user

class CreateUserForm(UserCreationForm):
    class Meta:

        model =User
        fields=["username", "password1", "password2"] # password2  for confirm password

# login a user

class LoginForm (AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

# -add user form

class createRecordForms(forms.ModelForm):
    class Meta:
        
        model =Record
        fields =['first_name', 'last_name', 'email', 'phone', 'city', 'country']

# update user record

class updateRecordForms(forms.ModelForm):
    class Meta:

        model =Record
        fields=['first_name', 'last_name', 'email', 'phone', 'city', 'country']