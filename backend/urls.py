"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from oauth2_provider import urls as oauth2_urls


urlpatterns = [
    path("admin/", admin.site.urls), 
    path('auth/', include('drf_social_oauth2.urls', namespace='drf')),
    path('o/', include(oauth2_urls)),
]


# curl -X POST -d "grant_type=convert_token&client_id=t8B9cmkmfQZNS9y1WnyuX2dHPsEm7EsvtSKkNHbk&backend=facebook&token=EAAQ9Kc5b0IABOZCujoZBOD5Io3W6jJN7AaXDoEoFt3xBVMiNPE3NL65FO3oVT2W07ljYwtMeO3tAn2y7H8VzRdnXdmU2nGzYzTgYpJ4YJwxkfJ20Vx66wv40DOKsusZCeZCXZA1nmeDLJglCqeZCUBfEYUb0fXt9D09iwmZCyI54nqgeVsYgtNZCm3ZBnKbMzecv10bkL0BARcQZDZD" http://127.0.0.1:8000/auth/convert-token