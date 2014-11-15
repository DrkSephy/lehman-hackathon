from django.shortcuts import render
from django.contrib.auth import authenticate, login
import pdb
import hashlib
from models import *


# Create your views here.

def signup(request):
	return render(request, "signup.html")

def login(request):
	pdb.set_trace()
	username = str(request.POST.get('username'))
	password1 = str(request.POST.get('password1'))
	password2 = str(request.POST.get('password2'))

	# if password1 != password2:
		#ERROR!!!!
	# else:
	user = User()
	user.username = username
	user.password = hashlib.sha1(password1).hexdigest()
	user.save()
	
	print "!!!!!!!"


# def createUser(request):

