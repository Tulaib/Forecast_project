from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app_one.models import user_Account
import geocoder
from geo_app.models import Geo_info
import urllib, json
from .serializer import *

g = geocoder.ip('me')

# Create your views here.
@api_view(["GET"])
def view_geo_tables(request):
    query= Geo_info.objects.all()
    ser=Geo_serializer(query,many=True)
    return Response(ser.data)




@api_view(["GET"])
def fetch_my_location(request):
    get_username =user_Account.objects.get(email=request.user)
    try:
        dict ={
            "latitude":g.lat,
            "longitude":g.lng,
            "IP":g.ip,
            "city":g.city
            }
        if get_username:
            query_update=Geo_info.objects.get_or_create(user=get_username,user_longitude=g.lng,user_latitude=g.lng
                ,user_ip=g.ip,user_city=g.city)
        return Response({"status":status.HTTP_200_OK,"Message":dict})
    except Exception as e:
        return Response({"status":False,"Message":e.__str__()})

@api_view(["GET"])
def fetch_weather_forecast(request):
    query1 =user_Account.objects.get(email=request.user)
    print(request.user)
    
    try:
        api_key='25c15cb1a0eef3fce56e8aea3c631087'
        url = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&appid={}".format(g.lat,g.lng,api_key)
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        if query1:
            query_updating = Geo_info.objects.get_or_create(user=request.user,weather_forecast=data)
        return Response(data)
    except Exception as e:
        return Response({"status":False,"message":e.__str__()})
