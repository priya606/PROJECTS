from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
        if request.method=="POST":
             name=request.POST['name']
             email=request.POST['email']
             subject=request.POST['subject']
             message=request.POST['message']
             recipient_list=[email]
             from_email=settings.EMAIL_HOST_USER
             send_mail(subject,message,email,recipient_list,name,from_email)
             return render(request,"contact.html",{"name":name})
        else:
             return render(request,"contact.html")

def resume(request):
    return render(request,"resume.html")

def services(request):
    return render(request,"services.html")

def portfolio(request):
    return render(request,"portfolio.html")