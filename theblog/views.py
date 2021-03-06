

from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView
from django.urls import reverse_lazy, reverse
# from django.http import HttpResponseRedirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import PostForm,CommentForm
from .models import Post,Comment,Profile


@login_required(redirect_field_name='members/login/')
def LikeView(request,pk):
    post=get_object_or_404(Post, id=request.POST.get('post_id'))
    liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('article',args=[str(pk)]))

class AboutView(TemplateView):
    template_name = "theblog/about.html"  

class ProfileView(LoginRequiredMixin ,ListView):
    login_url = 'members/login/'
    redirect_field_name ='about'
    model=Profile
    template_name = "theblog/profile.html"    

class HomeView(ListView):
    model=Post
    context_object_name = 'home_list'
    template_name='theblog/home.html'
    ordering=['-id']
    # paginate_by = 3

class MyPostsView(LoginRequiredMixin,ListView):
    login_url = '/members/login/'
    redirect_field_name = 'about'
    # model=Post
    context_object_name = 'myposts_list'
    template_name='theblog/myposts.html'
    ordering=['-id']
    def get_queryset(self):
        return Post.objects.filter(author_id=self.request.user)
    # def get_context_data(self, **kwargs):
    #     data = super().get_context_data(**kwargs)
    #     data['myposts'] = 'Post'
    #     return data
# class MyPostsView(ListView):
#     context_object_name = 'myposts_list'
#     template_name='theblog/myposts.html'
#     ordering=['-id']
#     def get_queryset(self):
#         return Post.objects.filter(id=self.request.user.id)

class ArticleDetailView(DetailView):
    
    model=Post
    template_name='theblog/article_detail.html'
    def get_queryset(self):
        self.articleki_id_ka_queryset = get_object_or_404(Post, id=self.kwargs['pk'])
        return Post.objects.filter(id=self.articleki_id_ka_queryset.id)
    def get_context_data(self,*args, **kwargs):
        context=super(ArticleDetailView,self).get_context_data(*args,**kwargs)
        stuff= get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes=stuff.total_likes()
        liked=False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked=True
         
        context['total_likes']=total_likes
        context['liked']=liked
        context['articleki_id'] = self.articleki_id_ka_queryset
        return context

class AddPostView(SuccessMessageMixin,LoginRequiredMixin,CreateView):
    login_url = '/members/login/'
    redirect_field_name = 'myposts'  # find out how it works?
    model=Post     #optional
    success_message = "Post added  successfully"
    form_class=PostForm
    template_name='theblog/add_post.html'
    def get_success_url(self):
        return reverse('myposts')
    # # fields='__all__'
class UpdatePostView(SuccessMessageMixin,LoginRequiredMixin,UpdateView):
    login_url = '/members/login/'
    redirect_field_name = 'about'
    model=Post     #optional
    # form_class=PostForm
    success_message = "Post updated successfully"
    template_name='theblog/update_post.html'
    fields=['title','text','snippet','header_image']
    def get_success_url(self):
        return reverse('myposts')

class DeletePostView(SuccessMessageMixin,LoginRequiredMixin,DeleteView):
    login_url = '/members/login/'
    redirect_field_name = 'about'
    success_message = "post deleted successfully"
    model=Post    
    success_url=reverse_lazy('home')
    # form_class=PostForm
    template_name='theblog/delete_post.html'
    def get_success_url(self):
        return reverse('myposts')
class AddCommentView(SuccessMessageMixin,LoginRequiredMixin,CreateView):
    login_url = '/members/login/'
    redirect_field_name = 'home'
    model=Comment
    success_message = "Comment added successfully"
    form_class=CommentForm
    template_name='theblog/add_comment.html'
    # fields='__all__'
    # def get_context_data(self, **kwargs):
    #         context = super(AddCommentView, self).get_context_data(**kwargs)
    #         context['something'] =Book.objects.filter(pk=self.kwargs.get('pk'))
    #         return context
    def get_context_data(self, *args,**kwargs):
            context = super().get_context_data(*args,**kwargs)
            # context['article_id'] = Post.objects.filter(id=self.kwargs['pk'])    # <<<---
            context['article_id'] = self.kwargs['pk']   # <<<---
            return context

    
  
    


    
# def home(request):
#     return render(request,'theblog/home.html',{})
#     # return HttpResponse("<H1> This is index Page</H1>")