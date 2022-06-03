from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(), label='username')
	email = forms.CharField(widget=forms.EmailInput(), label='email')
	password = forms.CharField(widget=forms.PasswordInput(), label='password')
	confirm_password = forms.CharField(widget=forms.PasswordInput(), label='confirm_password')

	def check_username(self):
		uname = self.cleaned_data['username']
		if User.objects.filter(username=uname).exists():
			raise forms.ValidationError('Username already exists')

		return self.uname

	def check_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError('Email already exists')
		return self.email

	def check_password(self):
		if password != confirm_password:
			raise forms.ValidationError("Password didn't match")
		return self.password

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(), label='username')
	password = forms.CharField(widget=forms.PasswordInput(), label='password')