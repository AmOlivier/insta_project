from main_app.models import NewPost, Comment
from profile_app.models import ProfileInfo
from django.contrib.auth.models import User
from django import forms


class FormNewPost(forms.ModelForm):
	class Meta:
		model = NewPost
		fields = ('description','picture')

class FormNewComment(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('text',)


class UserEditForm(forms.ModelForm):
  class Meta:
    model   = User
    fields  = ('first_name', 'last_name')
    widgets = {
      'first_name': forms.TextInput(attrs={
          'id': 'edit-first-name',
          'placeholder': 'First Name',
          'required': False,
        }),
      'last_name': forms.TextInput(attrs={
          'id': 'edit-last-name',
          'placeholder': 'Last Name',
          'required': False,
        }),
    }


class ProfileEditForm(forms.ModelForm):
  class Meta:
    model   = ProfileInfo
    fields  = ('bio','profile_pic','facebook_link')
    widgets = {
      'bio': forms.Textarea(attrs={
          'id': 'edit-bio',
          'placeholder': 'Bio...',
          'required': False,
        }),
    }
