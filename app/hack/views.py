import pdb
from forms import *
from models import *
from send_sms import sendMessage
from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as djangoLogin
import pdb
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect
from forms import *
from send_email import send_email

def signup(request):
	return render(request, "signup.html")

def login(request):
	username = str(request.POST.get('username'))
	password1 = str(request.POST.get('password1'))
	password2 = str(request.POST.get('password2'))


	#Case passwords does not match
	if password1 != password2:
		return render(request, 'register.html', {'msg':'Passwords not match', 'form':UserCreationForm()})
	
	#Create user
	else:
		user = User.objects.create_user(username=username, password=password1)
		user.save()
	
	return render(request, 'signin.html', {'form':LoginForm})



def signin(request):
	"""
	Redirects the user to the login form
	"""
	form = LoginForm()
	return render(request, 'signin.html', {'form':form})


@csrf_protect
def authenticateUser(request):
	"""
	This view authenticate the user and redirects him to the control panel
	"""
	username = str(request.POST.get('username'))
	password = str(request.POST.get('password'))
	
	user = authenticate(username=username, password=password)
	
	if user is not None:
		djangoLogin(request, user)
		return render(request, 'addclass.html',{'user':user})

	#Case username and password are incorrect
	else:
		return render(request, 'signin.html', {'form':LoginForm(), 'msg':'Incorrect username or password'})


@csrf_protect
def notify(request):
	if request.user.is_authenticated():
		return render(request, 'notify.html')


@csrf_protect
def sendNotification(request):

	if request.user.is_authenticated():
		print "\n\n\t\t\tNOTIFICATION SENT!!!\n\n"

	subject = 'Email Subject'
	msg_body = 'This is a test e-mail'
	recipient = ['nsbehackathon2014@gmail.com', 'cafe.mui@gmail.com', 'lsxliron@gmail.com', 'fitzgeralda2010@gmail.com', 'sephirothcloud1025@yahoo.com', 'ian.s.mcb@gmail.com']
	for r in recipient:
		send_email(subject, msg_body, r)	
	numbers = ['+13473282978']
	sendMessage(numbers)
	print "\n\n\t\t\tNOTIFICATION SENT!!!\n\n"


def addNumbers(request):
	if request.user.is_authenticated():
		print "\n\n\t\tAUTH\n\n\n"

def logoutUser(request):
	logout(request)
	return render(request, 'signin.html', {'form':LoginForm()})

def addClass(request):
	print "ADD NEWW CLASS PAGE"





def base(request):
	return render(request, 'base.html', )

