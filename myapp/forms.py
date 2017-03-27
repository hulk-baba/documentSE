from django import forms

from .models import Documents
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

	class Meta:
		model = Documents
		fields = ('Document' , 'keyword',)

class NewUser(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username' , 'password' ,'email',]