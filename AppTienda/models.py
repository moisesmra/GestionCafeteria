from django.db import models

# Create your models here.
class Combo(models.Model):
    nombre=models.CharField(max_length=50)
    cant_productos=models.PositiveSmallIntegerField()
    productos=models.TextField(max_length=500)
    precio=models.FloatField(max_length=6)

    def __str__(self):
        return self.nombre

        






