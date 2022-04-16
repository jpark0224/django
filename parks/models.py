from django.db import models

# Create your models here.


class Park(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
