from django.db import models


class CuentaBancaria(models.Model):

    #atributos propios
    saldo = models.FloatField()
    numero_tarjeta = models.CharField(max_length=16, blank= True , default='')
    cv = models.IntegerField()
    fecha_vencimiento = models.CharField(max_length=4,blank=True,default='')
