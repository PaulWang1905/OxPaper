from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from markdown import markdown
from django.utils.html import mark_safe
# Create your models here.
STATUS =(
    (0,"Draft"),
    (1,"Publish")
    )

    
class Category(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    order = models.IntegerField(unique=True)
    class Meta:
        verbose_name_plural = 'categories'
        ordering= ['-date_added']
    
    def __str__(self):
        return self.name

class Page(models.Model):
    """In this blog system, everything is a page, except category. This is a base model."""
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_pages")
    abstract = models.TextField()
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    date_added = models.DateTimeField(auto_now_add=True)   
    class Meta:
        verbose_name_plural = 'pages'
        ordering= ['-date_added']
    def get_content_as_markdown(self):
        return mark_safe(markdown(self.content, safe_mode='escape'))
    def __str__(self):
        return self.title

class Post(Page):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="posts")
    class Meta:
        verbose_name_plural = 'posts'
        ordering= ['-date_added']
    def __str__(self):
        return self.title

