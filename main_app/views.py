from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from .models import Post
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required




@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'



