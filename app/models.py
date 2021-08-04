from django.db import models

# Create your models here.
class Comercio(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    descripcion = models.CharField(max_length=500, null=True)
    direccion = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre

class Menu(models.Model):
    comercio = models.ForeignKey(Comercio, null=True, on_delete=models.SET_NULL)
    
    titulo = models.CharField(max_length=100, null=True)
    precio = models.PositiveIntegerField()
    descripcion = models.CharField(max_length=500, null=True)
    calificacion_media = models.FloatField(default=0)
    menu_pic  = models.ImageField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    categoria = models.ManyToManyField(Categoria)

    def __str__(self):
        return self.titulo