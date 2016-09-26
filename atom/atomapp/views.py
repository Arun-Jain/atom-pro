from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from . import forms
from django.contrib.auth import authenticate, login as auth_login, logout
from django.http import HttpResponse
from .models import formfill
from .forms import formfills

# Create your views here.
def index(request):
	return render(request, "index.html", {})

def login(request):
	login_of_user = forms.login_form(request.POST or None)
	if request.method=="POST":
		username = request.POST['username']
		password = request.POST['password']
		users = authenticate(username=username, password=password)
		if users is not None:
			if users.is_active:
				auth_login(request,users)
				return redirect("myprofile")
		else:
			return HttpResponse("username and password didn't match")
	

	context ={
		'login_of_user':login_of_user,
	}
	return render(request, 'login.html' ,context)


def signup(request):
	signup_of_user = forms.signupform(request.POST or None)
	if signup_of_user.is_valid():
		user = signup_of_user.save(commit=False)
		username = signup_of_user.cleaned_data['username']
		password = signup_of_user.cleaned_data['password']
		user.set_password(password)
		user.save()

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth_login(request,user)
				return redirect("myprofile")


	context = {
		'signup_of_user' : signup_of_user,
	}
	return render(request , 'signup.html', context)

def myprofile(request):
	form = formfills()
	context = {
		'form':form,
	}
	return render(request, 'myprofile.html', context)

def logout_view(request):
	logout(request)
	return HttpResponse("<h1>You Are Logged Out Successfully</h1>")

def students_view(request):
	context = {
	
	}
	return render(request, 'students.html', context)