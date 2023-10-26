from django.db import models

# Create your models here.

class Player(models.Model):
    ref = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    birth = models.DateField()
    position = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.id}"
    
class File(models.Model):
    #id = models.CharField(max_length=20, primary_key=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.id}"
    
class Session(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    drillTitle = models.CharField(max_length=100, null=True)
    totalTime = models.CharField(max_length=100, null=True)
    totalDistance = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    dtMin = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    zone4 = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    zone5 = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    zone6 = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    hsr = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    hsrMin = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    maxSpeed = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    spints = models.IntegerField(null=True)
    sprintDistance = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    accelerations = models.IntegerField(null=True)
    decelerations = models.IntegerField(null=True)
    accMin = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    decMin = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    hmlDistance = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    #idPlayer = models.ForeignKey(Player, on_delete=models.CASCADE, null=True) #TODO without foreign key, only a varchar
    idPlayer = models.CharField(max_length=20)
    idFile = models.ForeignKey(File, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return f"{self.name}, {self.date}, {self.idPlayer}, {self.idFile}"
