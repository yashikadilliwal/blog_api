
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/blog/', include('blog.urls')),
    path('api/user/', include('user.urls')),
    path("api-auth/", include("rest_framework.urls")),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #redirect the root URL to your admin or API root
    path('', RedirectView.as_view(url='admin/', permanent=False)),
    
]
