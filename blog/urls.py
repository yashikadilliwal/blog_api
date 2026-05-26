from rest_framework.routers import DefaultRouter
from .views import PostViewSet,CategoryViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('categories', CategoryViewSet,)

urlpatterns = router.urls
