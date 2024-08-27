from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Route for the home page
    path('get-news/', views.get_news, name='get_news'),  # Route for fetching news
]
