from django.db import models
import uuid 

# Create your models here.

class region(models.Model):
    Codregion = models.CharField(max_length=2, default=None, primary_key=True)
    RegionName = models.CharField(max_length=50, default=None)
    Area = models.FloatField(default = None)
    Lat = models.FloatField(default = None)
    Long = models.FloatField(default = None)
    Population = models.FloatField(default = None)
    
    def __str__(self):
        return self.Codregion
    

class comuna(models.Model):
    CodComuna = models.IntegerField(primary_key=True, default=None)
    Reg = models.ForeignKey(region, on_delete=models.CASCADE)
    ComunaName = models.CharField(max_length=50, default=None)
    Poblation = models.FloatField(default=None)

    def __str__(self):
        return self.ComunaName

class activesCase(models.Model):
    AcCod_comuna = models.ForeignKey(comuna, on_delete=models.CASCADE)
    AcDate = models.DateField(auto_now=False, auto_now_add=False, default=None)
    AcCantidad = models.FloatField(default=None)


class reportes(models.Model):
    RDate = models.DateField(auto_now=False, auto_now_add=False, default=None)
    RComuna = models.ForeignKey(comuna, on_delete=models.CASCADE)
    RConfirmed = models.FloatField(default=None)
    RActive = models.FloatField(default=None)
    #RDeath = models.FloatField(default=None)
    # RSymptomatic = models.FloatField(default=None)
    # RAsymptomatic = models.FloatField(default=None)
    #RTaza =models.FloatField(default=None)

class deathsporRegion(models.Model):
    DDate = models.DateField(auto_now=False, auto_now_add=False, default=None)
    DCodRegion = models.ForeignKey(region, on_delete=models.CASCADE)
    Ddeaths = models.FloatField(default=None)


class reportexcomuna(models.Model):
    region = models.CharField(max_length=50)
    cod_region = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50, default=None)
    comunaCodComuna = models.CharField(max_length=50)
    poblacion = models.CharField(max_length=50)
    #taza = models.IntegerField(default=None)
