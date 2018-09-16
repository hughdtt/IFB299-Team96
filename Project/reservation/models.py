from django.db import models
from datetime import datetime

# Create your models here.
class Reservation(models.Model):
	name = models.CharField(max_length=200)
	store_loc = models.CharField(max_length=200)
	pickup_dte = models.DateField(null=True, blank=True)
	return_dte = models.DateField(null=True, blank=True)
	def __str__(self):
	    return f'{self.name}, {self.store_loc}'
class Meta:
	ordering = ['store_loc']

def get_absolute_url(self):
    return reverse('Reservation-detail', args=[str(self.id)])


