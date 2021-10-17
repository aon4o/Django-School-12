from django.db import models


class Car(models.Model):
    color = models.CharField(max_length=100)
    made = models.DateTimeField(auto_now_add=True)
    brand = models.CharField(max_length=50)
    description = models.TextField()
