from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import RegistrationForm

# Create your views here.

# def Index(request):
# 	response = HttpResponse()
# 	response.writelines('<h1>Hello world</h1>')
# 	response.write('<h1>This is home page</h1>')
# 	return response

def Index(request):
	
	return render(request,"pages/home.html",{}) 

def Contact(request):
	return render(request,"pages/contact.html",{}) 

def Error404(request,exception):

	return render(request,'pages/error.html')

def Error500(request):
	return render(request,'pages/error.html')

def Register(request):
	form = RegistrationForm()
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			HttpResponseRedirect("/")
	return render(request,'pages/register.html',{'form':form})