from django.urls import path
from .views import scrape_view , home_view # Replace with your actual import


urlpatterns = [
    path('', home_view, name='home'),
    path('articles/scrape-news/', scrape_view, name='scrape'),
]
