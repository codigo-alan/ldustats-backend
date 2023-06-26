from django.db import models

# Create your models here.
""" class Player(models.Model):
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
        return f"{self.date}, {self.name}, {self.distance}" """
    
class Player(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=200)
    birth = models.DateField()
    position = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class File(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.id}, {self.date}"
    
class Session(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    distance = models.DecimalField(max_digits=4, decimal_places=2)
    idPlayer = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, to_field='id')
    idFile = models.ForeignKey(File, on_delete=models.CASCADE, null=True, to_field='id')

    def __str__(self):
        return f"{self.name}, {self.date}, {self.distance}, {self.idPlayer}, {self.idFile}"
