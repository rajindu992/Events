from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images')


