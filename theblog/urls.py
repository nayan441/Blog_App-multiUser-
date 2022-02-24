
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.HomeView.as_view(),name='home'),
    path('profile',views.ProfileView.as_view(),name='profile'),
    path('add_post',views.AddPostView.as_view(),name='add_post'),
    
    # path('about',views.AboutPage,name='about'),
    path('about',views.AboutView.as_view(),name='about'),
    path('myposts',views.MyPostsView.as_view(),name='myposts'),
    path('article/<int:pk>',views.ArticleDetailView.as_view(),name='article'),
    path('article/<int:pk>/comment',views.AddCommentView.as_view(),name='add_comment'),
    path('article/update/<int:pk>',views.UpdatePostView.as_view(),name='update_post'),
    path('article/remove/<int:pk>',views.DeletePostView.as_view(),name='delete_post'),
    path('like/<int:pk>',views.LikeView,name='like_post'),
]