
from django import forms

from .models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['author','title','text','snippet','header_image']
        widgets={
        # "author":forms.Select(attrs={'class':'form-control'}),
        "author":forms.TextInput(attrs={'class':'form-control','value':'', 'id':'currentUser', 'type':'hidden'}),
        "title":forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title'}),
        "text":forms.TextInput(attrs={'class':'form-control','placeholder':'Enter text'}),
        "snippet":forms.TextInput(attrs={'class':'form-control','placeholder':'enter snippet'}),
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['name','body','post_id']
        widgets={
        
        "post_id":forms.TextInput(attrs={'class':'form-control','value':'', 'id':'current_article', 'type':'hidden' }),
        # "post_id":forms.Select(attrs={'class':'form-control'}),
        "name":forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title'}),
        "body":forms.TextInput(attrs={'class':'form-control','placeholder':'Enter text'}),
        
        }