import pdb
from forms import *
from models import *
from send_sms import sendMessage
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as djangoLogin
import pdb
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect
from forms import *
from send_email import send_email
import datetime

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
		
		# return render(request, 'addclass.html',{'user':user, 'returnlist': AddClass.objects.all()})
		return redirect('/addClass', {'form':LoginForm(), 'msg':'Incorrect username or password'})

	#Case username and password are incorrect
	else:
		return render(request, 'signin.html', {'form':LoginForm(), 'msg':'Incorrect username or password'})
		


@csrf_protect
def notify(request):
	if request.user.is_authenticated():
		return render(request, 'notify.html', {'form':StudentDetails(), 'notifyForm':SendNotification()})


@csrf_protect
def sendNotification(request):
	if request.user.is_authenticated():
		# pdb.set_trace()

		className = str(request.POST.get('class_name'))
		note = request.POST.get('note')

		subject = "{cn} is canceled".format(cn=className)
		msg_body = 'Dear students, our class is canceled.\n\n\n{note}'.format(note=note)
		recipient = AddClass.objects.filter(class_name=className)[0].students
	
		notif = Notification()
		notif.class_name = className
		notif.timeStamp = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M %p")
		notif.note=note
		notif.save()

		for rec in recipient.all():
			send_email(subject, msg_body, str(rec.email))	
			sendMessage(className, rec.number)


		# return render(request, 'notify.html', {"notifyMsg":"Messages sent successfully."})
		return render(request, 'addclass.html',{'user':request.user, 'returnlist': AddClass.objects.all(), 'studentDetailsForm':StudentDetails(), 'notifyForm':SendNotification(), "notifyMessage":"Messages sent successfully"})




def addNumbers(request):
	if request.user.is_authenticated():
		return render(request, 'addStudents.html')
	else:
		return render(request, 'signin.html', {'form':LoginForm()})

def logoutUser(request):
	logout(request)
	return render(request, 'signin.html', {'form':LoginForm()})

def addClass(request):
	# print "ADD NEWW CLASS PAGE"
	return render(request, 'addclass.html',{'user':request.user, 'returnlist': AddClass.objects.all(), 'studentDetailsForm':StudentDetails(), 'notifyForm':SendNotification()})


def base(request):
	return render(request, 'studentview.html' )


def addDetailsToDB(request):
	# pdb.set_trace()
	phoneNumbers = str(request.POST.get('phoneNumbers'))
	emails = request.POST.get('emails')
	className = request.POST.get('className')

	phoneNumbers = phoneNumbers.split(', ')
	emails = emails.split(', ')
	
	addClass = AddClass.objects.get_or_create(class_name=className)[0]
	
	for number, email in zip(phoneNumbers, emails):
		student = StudentInfo.objects.get_or_create(number=str(number), email=str(email))	[0]
		addClass.students.add(student)
	
	# return render(request, 'addclass.html', {'user':request.user, 'returnlist': AddClass.objects.all(), 'studentDetailsForm':StudentDetails(), "addNumbersMessage":"Numbers added successfully"})
	return redirect('/addClass', {'user':request.user, 'returnlist': AddClass.objects.all(), 'studentDetailsForm':StudentDetails(), "addNumbersMessage":"Numbers added successfully"})

def userFeed(request):
	return render(request, 'studentview.html', {'notifications':Notification.objects.all()[::-1], 'searchFeedForm':SearchFeedForm()})
		
@csrf_protect
def searchFeed(request):
	className = request.POST.get('className')
	return render(request, 'studentview.html', {'notifications':Notification.objects.filter(class_name=className)[::-1]})







