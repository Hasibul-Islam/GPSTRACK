from django.db import models

class Gps(models.Model):
	CarID = models.CharField(max_length=30)
	Latitude = models.CharField(max_length=30)
	Longitude = models.CharField(max_length=30)

	def __str__(self):
		return self.CarID
# Create your models here.
