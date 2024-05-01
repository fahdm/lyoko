from django.contrib.auth import authenticate,login
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView, CreateView
from .models import Post
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy




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

class AddPostView(CreateView):
    model = Post
    template_name = 'post.html'
    fields = ['title', 'title_tag','body']
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        messages.success(self.request,'post created successfully')
        return super().form_valid(form)



