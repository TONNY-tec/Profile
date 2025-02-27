import os

from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.http import HttpResponse, request
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.template import context
from django.core.mail import send_mail
from django.conf import settings

import personal
from personal.forms import PersonalForms
from personal.models import Personal


# my views.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def resume(request):
    return render(request, 'resume.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def service(request):
    return render(request, 'service.html')

def succesful(request):
    return render(request, 'succesful.html')

# def contact(request):
#     form = PersonalForms()
#     if request.method == 'POST':
#         form= PersonalForms(request.POST , request.FILES)
#         if form.is_valid():
#             personal =form.save(commit=False)
#             personal.save()
            
#             subject = f"New Contact Form Submission from {personal.name}"
#             body = f"Name: {personal.name}\nEmail: {personal.email}\n\nMessage:\n{personal.message}"
#             from_email = settings.EMAIL_HOST_USER  # Sender (your email)
#             recipient_list = ['tonnysafari3@gmail.com']  # Replace with the email that should receive the messages

#             # Send email
#             send_mail(subject, body, from_email, recipient_list)

#             return redirect('index')
#         else:
#             form = PersonalForms()
#     return render(request, 'contact.html', {'form':form})

def contact(request):
    form = PersonalForms()
    if request.method == "POST":
        form = PersonalForms(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Construct the email content
            email_subject = f"New Contact Form Submission: {subject}"
            email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

            # Send email to admin
            send_mail(email_subject, email_message, settings.DEFAULT_FROM_EMAIL, ['tonnysafari3@gmail.com'])

            return redirect('succesful')  # Redirect to a success page
    else:
        form = PersonalForms()

    return render(request, "contact.html", {"form": form})