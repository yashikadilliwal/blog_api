from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Post(models.Model):
    author=models.ForeignKey(User , on_delete=models.CASCADE)
    category  =models.ForeignKey(Category , on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    thumbnail_image = models.ImageField(upload_to='blog_thumbnails/',null=True,blank=True
    )

  
    slug = AutoSlugField(
        populate_from='title',
        unique=True,
        always_update=False # bcz we dont want to break the url again and again, do we?
    )
    content = CKEditor5Field(
    'Content',
    config_name='extends'
)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created_at']
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"


    def __str__(self):
        return self.title
    
class PostImage(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='images'
    )

    image = models.ImageField(upload_to='blog_images/')
    
    def __str__(self):
        return f"{self.post.title} image"

class Comment(models.Model):
    post = models.ForeignKey(Post,  on_delete=models.CASCADE)
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    post = models.ForeignKey(Post,  on_delete=models.CASCADE)

    # i added this bcz one user can only like once
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'post'],
                name='unique_post_like'
            )
        ]



