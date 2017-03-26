from django import forms

from .models import Documents

class PostForm(forms.ModelForm):

	class Meta:
		model = Documents
		fields = ('Document' , 'keyword',)