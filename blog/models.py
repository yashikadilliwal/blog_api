from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name=models.CharField()

    def __str__(self):
        return self.name


class Post(models.Model):
    author=models.ForeignKey(User , on_delete=models.CASCADE)
    category  =models.ForeignKey(Category , on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"


    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Post,  on_delete=models.CASCADE)
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    content = models.TextField()


class Like(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    post = models.ForeignKey(Post,  on_delete=models.CASCADE)



