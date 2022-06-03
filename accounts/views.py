from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, FormView, View
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from accounts.forms import RegisterForm, LoginForm



# Create your views here.
class HomeTemplate(TemplateView):
	template_name = 'accounts/base.html'
	success_url = '/'

#register page
class RegisterPage(SuccessMessageMixin,FormView):
	template_name = 'register/register.html'
	success_url = reverse_lazy('accounts:register-page')
	form_class = RegisterForm
	success_message = "Register Successfull"

	def form_valid(self, form):
		uname = form.cleaned_data['username']
		email = form.cleaned_data['email']
		pword = form.cleaned_data['password']

		User.objects.create_user(uname, email, pword)

		return super().form_valid(form)

	def get_success_message(self, cleaned_data):
		return self.success_message % cleaned_data


#login page
class LoginPage(FormView):
	template_name = 'registration/login.html'
	success_url = reverse_lazy('hospitalmanagementapp:dashboard-page')
	form_class = LoginForm

	def form_valid(self, form):
		uname = form.cleaned_data['username']
		pword = form.cleaned_data['password']

		usr = authenticate(username=uname, password=pword)

		if usr is not None:
			login(self.request, usr)
		else:
			return render(self.request, self.template_name,{
				'error':'Invalid username or password',
				'form':form
				})

		return super().form_valid(form)


#logout
class LogoutPage(View):
	def get(self, request):
		logout(request)
		return redirect('accounts:home-page')