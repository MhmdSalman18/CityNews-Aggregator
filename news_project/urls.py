"""
URL configuration for news_project project.

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
# news_project/urls.py

from django.contrib import admin
from django.urls import path
from news_app import views  # Replace 'your_app' with the actual name of your Django app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Route for the home page
    path('get-news/', views.get_news, name='get_news'),  # Route for fetching news
]
