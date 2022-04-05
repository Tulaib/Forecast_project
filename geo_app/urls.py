from django.urls import path
from .views import fetch_my_location,fetch_weather_forecast,view_geo_tables

app_name = 'weather_forecast'
urlpatterns = [
    path('fetch_my_location/',fetch_my_location),
    path('weather_forecast_for_me/',fetch_weather_forecast),
    path('all_geos/',view_geo_tables)
]