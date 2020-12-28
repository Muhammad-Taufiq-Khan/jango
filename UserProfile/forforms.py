from django import forms
from .models import *

class LoginFrom(forms.Form):
   user_name = forms.CharField(max_length=200, label='Username')
   user_pass = forms.CharField(max_length=100, label='Password',
                               widget=forms.PasswordInput)

class SignupForm(forms.ModelForm):
   user_na = forms.CharField(max_length=100, label='Username')
   user_pass = forms.CharField(max_length=100,
                               widget=forms.PasswordInput, label='Password')
   user_pass2 = forms.CharField(max_length=100,
                                widget=forms.PasswordInput, label='Confirm Password')
   class Meta:
       model = ProfileUser
       fields = ("user_na","user_pass","user_pass2","email","phone","address","image")


class UserEditForm(forms.ModelForm):
    class Meta:
        model = ProfileUser
        fields = ["email", "phone","address","image"]

class ChangePassForm(forms.Form):
    old_pass = forms.CharField(max_length=100,
                                widget=forms.PasswordInput, label='old Password')
    user_pass = forms.CharField(max_length=100,
                                widget=forms.PasswordInput, label='New Password')
    user_pass2 = forms.CharField(max_length=100,
                                 widget=forms.PasswordInput, label='Confirm Password')

