from django.contrib import admin
from .models import Post , Category,PostImage # Import your model

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(PostImage)
