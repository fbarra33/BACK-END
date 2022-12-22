from django.db import models
from django.utils import timezone

# Create your models here.

estado = [    
    ("RESERVADO", "RESERVADO"),    
    ("COMPLETADA", "COMPLETADA"),    
    ("ANULADA", "ANULADA"),    
    ("NO ASISTEN", "NO ASISTEN")]

class Participantes(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    fecha_inscripcion = models.DateField()
    hora_inscripcion = models.TimeField()
    institucion = models.CharField(max_length=50)
    estado = models.CharField(max_length=50, choices = estado)
    observacion = models.TextField(blank=True)


class Instituciones(models.Model):
    id = models.AutoField(primary_key=True)
    institucion = models.CharField(max_length=50)
    


