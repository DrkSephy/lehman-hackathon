from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(max_length=20)
	# password = forms.PasswordInput()
	password = forms.CharField(label=("Password"), widget=forms.PasswordInput, required=False)