import os

from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.http import HttpResponse, request
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.template import context

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

def contact(request):
    return render(request, 'contact.html')
