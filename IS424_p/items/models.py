from django.db import models
from django.contrib.auth.models import User 

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    users = models.ManyToManyField(User, related_name='items')  

    def __str__(self):
        return self.name