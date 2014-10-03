from django.db import models
import datetime
# Create your models here.
class Evento(models.Model):
    nombre=models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

    class Admin:
        pass

TIPOS_PRIORIDAD=(
    (1,'Baja'),
    (2,'Normal'),
    (3,'Alta')
)

class Tarea(models.Model):
    titulo=models.CharField(max_length=250)
    completado=models.BooleanField(default=False)
    fecha_creacion=models.DateTimeField(auto_now_add=True)
    prioridad=models.IntegerField(choices=TIPOS_PRIORIDAD,default=2)
    evento=models.ForeignKey(Evento,blank=True,null=True)

    def __str__(self):
        return self.titulo