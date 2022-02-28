
from django.urls import reverse
from django.db import models
from django.utils import timezone
# from django.urls import reverse
from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

# # User=get_user_model()


class Profile(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio=models.TextField(null=True,default="No Bio  Available")
    profile_pic=models.ImageField(null=True,blank=True,upload_to='profile_pic/')
    facebook_url=models.CharField(max_length=200,null=True,blank=True,)
    insta_url=models.CharField(max_length=200,null=True,blank=True,)
    linkedin_url=models.CharField(max_length=200,null=True,blank=True,)

    def __str__(self):
        return str(self.user)
    def get_absolute_url(self):
        return reverse('home',args=(str(self.id)))


class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    header_image=models.ImageField(null=True,blank=True,upload_to="image/")
    # text=models.CharField(max_length=500)
    snippet=models.CharField(max_length=500, default='click above to read post')
    text=RichTextField()
    creation_date=models.DateTimeField(auto_now_add=True)
    publish_date=models.DateTimeField(auto_now_add=True)
    likes=models.ManyToManyField(User,related_name='post_likes')

    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return f'Title--{self.title} >> by Username--  {self.author}'
    def get_absolute_url(self):
        return reverse('home')
    # def get_absolute_url(self):
    #     return reverse('article',args=(str(self.id)))
class Comment(models.Model):
    post_id=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE) #manytoone
    name=models.CharField(max_length=20,)
    body=models.TextField(null=True, blank=True)
    date_added=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f'{self.post_id.title}--{self.name}'
    def get_absolute_url(self):
        return reverse('home')
