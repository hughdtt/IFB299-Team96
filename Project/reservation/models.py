from django.db import models
from datetime import datetime

#Model for reviews 
class Reviews(models.Model):
    review = models.TextField(max_length = 400)
    def __str__(self):
        return str(self.review)
