from django.contrib.auth import authenticate,login
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView, CreateView,UpdateView,DeleteView
from .models import Post,Category
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy




@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

#def home(request):
    return render(request, 'home.html', {})

def CategoryView(request,cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request,'categories.html',{'cats': cats, 'category_posts': category_posts})


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-created_at']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post
    # form_class = PostForm
    template_name = 'post.html'
    fields = '__all__'
    fields = ['title','body']
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        messages.success(self.request,'post created successfully')
        return super().form_valid(form)

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'
    

class UpdatePostView(UpdateView):
    model = Post
    # form_class = EditForm
    template_name = 'update_post.html'
    fields = ['title','title_tag', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
