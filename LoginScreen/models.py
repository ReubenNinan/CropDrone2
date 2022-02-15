from django.db import models
from django.contrib.auth.models import User, auth

class GPSData(models.Model):
    user_name = models.CharField(max_length=100)
    plant_name = models.CharField(max_length=100)
    plant_id = models.IntegerField()
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    X_Coords = models.DecimalField(max_digits=9, decimal_places=6)
    Y_Coords = models.DecimalField(max_digits=9, decimal_places=6)
    img = models.ImageField(upload_to = 'DB Pictures') 
    # desc = models.TextField(null = True), 


