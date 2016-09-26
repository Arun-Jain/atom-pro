from django import forms
from django.contrib.auth.models import User
from .models import formfill

class login_form(forms.ModelForm):
	class Meta:
		model = User
		widgets = {
		'username' : forms.TextInput(attrs = {'placeholder': 'Username','required': 'True'}),
		'password' : forms.PasswordInput(attrs = {'placeholder': 'Password','required': 'True'}),
		}

		fields = ['username', 'password']


class signupform(forms.ModelForm):
	class Meta:
		model = User
		widgets = {
		'username' : forms.TextInput(attrs = {'placeholder': 'Username','required': 'True'}),
		'email'    : forms.EmailInput(attrs = {'placeholder': 'E-Mail','required': 'True'}),
		'password' : forms.PasswordInput(attrs = {'placeholder': 'Password','required': 'True'}),

			}
		fields = ['username', 'email', 'password']
	def clean_username(self):
		username = self.cleaned_data['username']
		if User.objects.filter(username=username).exists():
			raise forms.ValidationError("That Username Is Already Taken")
		return username

class formfills(forms.ModelForm):
	class Meta:
		model = formfill
		widgets = {
		'full_name' : forms.TextInput(attrs = {'placeholder': 'Full Name','required': 'True'}),
		'email' : forms.EmailInput(attrs = {'placeholder': 'Email','required': 'True'}),
		'college_name' : forms.TextInput(attrs = {'placeholder': 'College Name','required': 'True'}),
		'college_place' : forms.TextInput(attrs = {'placeholder': 'College Place','required': 'True'}),
		'phone_no' : forms.NumberInput(attrs = {'placeholder': 'Phone Number','required': 'True'}),
		'skill1' : forms.TextInput(attrs = {'placeholder': 'Skill','required': 'True'}),
		'branch' : forms.TextInput(attrs = {'placeholder': 'Branch','required': 'True'}),
		'year' : forms.DateInput(attrs = {'placeholder': 'Year','required': 'True'}),
		'post' : forms.TextInput(attrs = {'placeholder': 'Description of Yours','required': 'True'}),
		}
		fields = [ 'full_name','email','college_name','college_place','phone_no','skill1','branch','year','post','profile_image']
