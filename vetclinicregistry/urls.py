"""vetclinicregistry URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from clinic.views import (
    registration_view,
    logout_view,
    home_screen_view,
    login_view,
    account_view
)
#from clinic.viewss import animals

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clinic/', include('clinic.urls')),
    path('register/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('', home_screen_view, name="home"),
    path('login/', login_view, name="login"),
    path('account/', account_view, name="account"),
]

#MEDIA_URL = '/media/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')