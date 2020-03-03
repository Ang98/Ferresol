from django.db import models

from .Cotizacion import *
from .CuentaBancaria import *

class OrdenDeCompra(models.Model):

    #atributos foraneos
    id_cuenta_bancaria= models.ForeignKey(CuentaBancaria, on_delete=models.CASCADE)
    id_cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE)

    #atributos propios
    nombre_recepcionista = models.CharField(max_length=45, blank=True, default='')
    fecha = models.DateField(auto_now_add=True)
    direccion = models.CharField(max_length=45, blank=True, default='')
    distrito = models.CharField(max_length=45, blank=True, default='')
    provincia= models.CharField(max_length=45, blank=True, default='')
    departamento = models.CharField(max_length=45, blank=True, default='')
    nombre_comprador= models.CharField(max_length=45, blank=True, default='')


