from django.shortcuts import render
from django.contrib.auth import authenticate, login
import pdb
from django.contrib.auth.forms import UserCreationForm
from models import *
from django.views.decorators.csrf import csrf_protect
from forms import *



# Create your views here.

def signup(request):
	return render(request, "signup.html")

def login(request):
	username = str(request.POST.get('username'))
	password1 = str(request.POST.get('password1'))
	password2 = str(request.POST.get('password2'))

	if password1 != password2:
		return render(request, 'register.html', {'msg':'Passwords not match', 'form':UserCreationForm()})
	
	else:
		user = User.objects.create_user(username=username, password=password1)
		user.save()
	
	return render(request, 'signin.html')


def signin(request):
	form = LoginForm()
	return render(request, 'signin.html', {'form':form})

@csrf_protect
def authenticateUser(request):
	username = str(request.POST.get('username'))
	password = str(request.POST.get('password'))
	
	user = authenticate(username=username, password=password)
	if user is not None:
		print "DSJFHSDKJHFSKJDHFKLJSDFHKLSDJHFLSKDJHFDSJK"

	else:
		return render(request, 'signin.html', {'form':LoginForm(), 'msg':'Incorrect username or password'})



