from django.db import models

class Cotizacion(models.Model):

    #atributos propios
    costo_total = models.FloatField()
    cantidad_productos = models.IntegerField()