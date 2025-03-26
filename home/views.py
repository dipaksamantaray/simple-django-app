from django.shortcuts import render,redirect 
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    return render (request,'index.html')
    # return HttpResponse("this is the home page")
def about(request):
    return render (request,'about.html')

    # return HttpResponse("this is the about page")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mob = request.POST.get('mob')
        password = request.POST.get('password')
        contact = Contact(name=name,email=email,mob=mob,password=password)
        contact.save()
        messages.success(request, "The form will be submitted !")
        return redirect('contact')
    return render (request,'contact.html')

    # return HttpResponse("this is the services page")

def services(request):
    return render (request,'services.html')

    # return HttpResponse("this is the services page")
    

    