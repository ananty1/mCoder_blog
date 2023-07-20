from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home/home.html')

def about(request):
    messages.success(request,'This is our about Page')
    return render(request,'home/about.html')

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if(len(name)<2 or len(email)<4 or len(phone)<10 or len(content)<4):
            messages.error(request,'Please fill the form Correctly')
        
        else:
            contact = Contact(name = name,email = email,phone = phone,content = content)
            contact.save()
            messages.success(request,'Your Form is submitted succesfully')

    return render(request,'home/contact.html')



