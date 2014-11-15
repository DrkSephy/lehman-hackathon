from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(max_length=20)
	# password = forms.PasswordInput()
	password = forms.CharField(label=("Password"), widget=forms.PasswordInput, required=False)


class StudentDetails(forms.Form):
	phoneNumbers = forms.CharField(widget=forms.Textarea)
	emails = forms.CharField(widget=forms.Textarea)
	className = forms.CharField(max_length=20)

class SendNotification(forms.Form):
	class_name=forms.CharField(widget=forms.TextInput(attrs={'class' : 'btn-selector'}))
	note = forms.CharField(widget=forms.Textarea)

class SearchFeedForm(forms.Form):
	className = forms.CharField(max_length=20)