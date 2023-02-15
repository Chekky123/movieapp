from django.db import models


# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=2500)
    description = models.TextField(max_length=25000)
    year = models.IntegerField()
    img = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name
