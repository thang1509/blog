from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from ckeditor.fields import RichTextField
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.signals import pre_save
from blog.utils import unique_slug_generator


# Create your models here.
class Categories(models.Model):
    categoryname = models.CharField(max_length=255)

    def __str__(self):
        return self.categoryname
class Post(models.Model):
    author = models.ForeignKey(User,on_delete=CASCADE,default='auth.User')
    title = models.CharField(max_length=255)
    tacgia = models.CharField(max_length=255,null=True)
    title_tag = models.CharField(max_length=255, default='Blog Post')
    slug = models.SlugField(max_length=255, null=True, blank=True)
    img = models.ImageField(upload_to='blog',null = True)
    body = RichTextField(blank=False, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    download = models.CharField(max_length=500,null=True)
    category = models.ForeignKey(Categories, null=True, on_delete=models.PROTECT, related_name='category_set')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Post)

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments',on_delete=CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post,self.name)