import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings


def index(request):
    # Initially, no location is provided, so news may not be fetched here
    return render(request, 'index.html', {'news': [], 'location_name': 'Default Location'})

import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

def get_news(request):
    location_name = request.GET.get('location', 'New York')  # Default to 'New York' if no location is provided
    news_data = []

    # API URL and parameters
    news_api_url = 'https://gnews.io/api/v4/search'
    params = {
        'q': location_name,
        'token': settings.GNEWS_API_KEY,
        'lang': 'en'
    }
    
    try:
        response = requests.get(news_api_url, params=params)
        response.raise_for_status()
        news_data = response.json().get('articles', [])
        
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

    return JsonResponse({'articles': news_data})
