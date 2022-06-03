from django.urls import path
from accounts.views import HomeTemplate, RegisterPage, LoginPage,LogoutPage

app_name = 'accounts' #custom url

urlpatterns = [
	path('', HomeTemplate.as_view(), name='home-page'),
	path('registerPage/',RegisterPage.as_view(),name='register-page'),
	path('loginPage/', LoginPage.as_view(), name='login-page'),
	path('logoutPage/', LogoutPage.as_view(), name='logout-page')
]