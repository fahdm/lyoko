from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session



@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

# Create your views here.
def home(request):
    return render(request, 'home.html')



