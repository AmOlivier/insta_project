from django.urls import path 
from . import views

app_name = 'login_app'

urlpatterns = [
	path('login/', views.log_in, name='loginpage'),
	path('signup/', views.signup, name='signup'),
	path('logging_out/', views.logging_out, name='logging_out'),
]