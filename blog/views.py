from django.shortcuts import render
from rest_framework import generics, mixins, viewsets
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import(
    Post)
from .serializer import (
    PostSerializer)


#  -----------------------------better way to do this-----------------------

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



# class PostView(mixins.ListModelMixin, viewsets.GenericViewSet):
#     queryset=Post.objects.all()
#     serializer_class=PostSerializer
#     http_method_names=['get']

# class PostCreate(mixins.CreateModelMixin, viewsets.GenericViewSet):
#     queryset=Post.objects.all()
#     serializer_class=PostSerializer
#     http_method_names=['post']

# class PostUpdateDelete(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin, viewsets.GenericViewSet):
#     queryset=Post.objects.all()
#     serializer_class=PostSerializer
#     http_method_names=['post']