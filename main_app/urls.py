from django.urls import path
from .import views
from .views import HomeView, ArticleDetailView,AddPostView,UpdatePostView,DeletePostView

urlpatterns = [
    # path('', views.home, name='home'),
    
    path('accounts/logout/', views.logout_view, name='logout'),
    path('',HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name = 'article-detail'),
    path('post/',AddPostView.as_view(), name='post'),
    path('article/edit/<int:pk>',UpdatePostView.as_view(), name='edit_post'),
    path('article/<int:pk>/delete',DeletePostView.as_view(), name='delete_post'),
]