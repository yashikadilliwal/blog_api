from django.contrib import admin
from .models import Post , Category # Import your model

admin.site.register(Post)
admin.site.register(Category)
