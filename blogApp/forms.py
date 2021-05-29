from django import forms
from django.db.models import fields 
from .models import Comment, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','tacgia','author','img','body','category','download')
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['img'].required = False

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('__all__')