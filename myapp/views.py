from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from rest_framework import viewsets 
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Documents
from .forms import PostForm, NewUser
from .serializers import DocumentSerializers
import urllib
from django.views.static import serve
import os
import requests
from requests.auth import HTTPDigestAuth
import json
from urllib2 import Request, urlopen, URLError

# Create your views here.

@login_required(login_url='http://127.0.0.1:8000/myapp/login')
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
@login_required(login_url='http://127.0.0.1:8000/myapp/login')
def detail(request):

	if request.method == "POST":
		form = PostForm(request.POST,request.FILES)
		if form.is_valid():
			print "true doc is" , request.FILES['Document']
			print "true key is" , request.POST['keyword']
			post = form.save(commit = True)
			path = "/home/atul/DocumentSearchEngine/DocumentSearchEngine/uploads/uploads"
			os.chdir(path)
			os.system("git init")
			os.system("git add .")
			os.system('git commit -m "Random" ')
			os.system("git push -f origin master")
			path = "/home/atul/DocumentSearchEngine"
			os.chdir(path)
			post.save()
	else:
		form = PostForm()
	return render(request,'detail.html',{'form':form})

def show(request,murga):
	print "request is" , request
	print "ans is ",murga
	url = "https://github.com/hulk-baba/uploads/raw/master/"
	url = url + murga 
	os.system("wget " + url)
	return HttpResponse("Succefully Downloaded")

class DocumentViewSet(viewsets.ModelViewSet):
	queryset = Documents.objects.all()
	serializer_class = DocumentSerializers

@login_required(login_url='http://127.0.0.1:8000/myapp/login')
def search(request):
	if request.method == "POST":
		query = request.POST['query']
		print "query is ",query
		url = "http://localhost:8000/myapp/api/v1/doc/?format=json"
		myResponse = requests.get(url)
		if(myResponse.ok):
			jData = json.loads(myResponse.content)
			print "Ye hai game of thrones ki kahani\n"
			jData =  jData["objects"]
			for every in jData:
				for key in every:
					print key + " : " + str(every[key]) + "\n"
					if(key == "keyword"  and every[key] == query):
						print "found a match for " + every['Document']

		ans = Documents.objects.all().filter(keyword=query)
		return render(request,'show.html',{'ans' : ans})

	return render(request,'search.html',{})	

def newUser(request):
	if(request.method == "POST"):
		form = NewUser(request.POST)
		if(form.is_valid()):
			post = form.save()
			post.save()

	else:
		form = NewUser()
	return render(request,'newuser.html',{"form":form})

def login(request):
	if(request.method == "POST"):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username = username , password = password)

		if user is not None:
			auth_login(request,user)
			# redirect('http://127.0.0.1:8000/myapp/')
			return HttpResponseRedirect(reverse('myapp:index'))

		else:
			return HttpResponse("LOGIN FAILED")

	return render(request,'login.html',{})

@login_required(login_url='http://127.0.0.1:8000/myapp/login')
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('myapp:login'))