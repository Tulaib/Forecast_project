from django.db import models
from app_one.models import user_Account
# Create your models here.
class Geo_info(models.Model):
    user = models.ForeignKey(user_Account,on_delete=models.CASCADE)
    user_longitude = models.IntegerField(null=True,blank=True)
    user_latitude = models.IntegerField(null=True,blank=True)
    user_ip = models.GenericIPAddressField(null=True,blank=True)
    user_city = models.CharField(max_length=100, null=True,blank=True)
    requested_time = models.DateField(auto_now=True)
    weather_forecast = models.JSONField()
    
