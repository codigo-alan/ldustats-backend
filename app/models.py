from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=200)
    birth = models.DateField()
    position = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Session(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    distance = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.date}, {self.name}, {self.distance}"