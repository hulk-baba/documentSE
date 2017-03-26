from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from rest_framework import viewsets

from .models import Documents
from .forms import PostForm
from .serializers import DocumentSerializers
import urllib
from django.views.static import serve
import os
# Create your views here.

def index(request):
	list_of_docs = Documents.objects.all();
	template  = loader.get_template('myapp/index.html')
	context = {
		'list_of_docs' : list_of_docs,
	}
	return HttpResponse(template.render(context,request))

# def detail(request):
# 	template  = loader.get_template('myapp/detail.html')
# 	context = {}
# 	return HttpResponse(template.render(context,request))

def detail(request):

	if request.method == "POST":
		form = PostForm(request.POST,request.FILES)
		if form.is_valid():
			print "true doc is" , request.FILES['Document']
			print "true key is" , request.POST['keyword']
			post = form.save(commit = True)
			post.save();
			os.system("cd DocumentSearchEngine/uploads/uploads")
			os.system("git init")
			os.system("git add .")
			os.system('git commit -m "Random" ')
			os.system("git remote add https://github.com/hulk-baba/uploads.git")
			os.system("git remote -v")
			os.system("git push origin master")
	else:
		form = PostForm()
	return render(request,'detail.html',{'form':form})

def show(request,murga):
	print "request is" , request
	print "ans is ",murga
	url = "https://raw.githubusercontent.com/hulk-baba/uploads/master/"
	url = url + murga 
	os.system("wget " + url)
	return HttpResponse("Succeffully Downloaded")

class DocumentViewSet(viewsets.ModelViewSet):
	queryset = Documents.objects.all()
	serializer_class = DocumentSerializers