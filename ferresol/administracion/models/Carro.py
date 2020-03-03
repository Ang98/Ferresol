from django.db import models
from .Producto import *
from .Cotizacion import *

class Carro(models.Model):
    # atributos foraneos
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, blank=True)
    id_cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE, null=True, blank=True)

    # atributos propios
    cantidad = models.IntegerField()
    subtotal = models.IntegerField()
