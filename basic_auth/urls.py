"""basic_auth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from library.views import GetBookListAPIVIew

from basic_auth import settings

urlpatterns = [
    path('', RedirectView.as_view(url='library/books/')),
    path('admin/', admin.site.urls, name='admin_panel'),
    path('account/', include('account.urls')),
    path('library/', include('library.urls')),

    path('api-token-auth/', obtain_jwt_token, name='token_obtain_pair'),
    path('api-token-refresh/', refresh_jwt_token, name='token_refresh'),
    path('api-token-verify/', verify_jwt_token),

    path('book-list-api/', GetBookListAPIVIew.as_view())

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
