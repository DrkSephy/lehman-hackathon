from django.shortcuts import render
from django.contrib.auth import authenticate, login




# Create your views here.

def signup(request):
	return render(request, "signup.html")

def login(request):
	print "!!!!!!!"
