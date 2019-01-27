from django import forms
from django.contrib.auth.models import User
from profile_app.models import ProfileInfo
import datetime


class UserForm(forms.ModelForm):
	password = forms.CharField(widget= forms.PasswordInput)
	class Meta:
		model = User
		help_texts = { 'username': None}
		fields = ('username', 'email', 'password')


class LoginForm(forms.Form):
	username = forms.CharField(max_length=150)
	password = forms.CharField(widget=forms.PasswordInput())
	def clean(self):
		all_clean_data = super().clean()
		return all_clean_data

class UserProfileInfoForm(forms.ModelForm):
	class Meta:
		model = ProfileInfo
		fields = ('bio', 'profile_pic')
