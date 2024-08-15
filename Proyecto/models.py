
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=150, unique=True)
    correo_electronico = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128)
    
class DatosAlmacenados(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.FloatField()
    waist = models.FloatField()
    hips = models.FloatField()
    neck = models.FloatField()
    energy_level = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.date}"
    

