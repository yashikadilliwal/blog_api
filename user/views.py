from rest_framework import mixins, viewsets
from django.contrib.auth.models import User
from .serializer import RegisterSerializer

class RegisterViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer