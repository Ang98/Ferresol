from django.db import models
#TRYU
# Create your models here.

class Producto(models.Model):

    #atributos propios
    nombre = models.CharField(max_length=45, blank=True, default='')
    precio = models.IntegerField(blank=True,null=True)
    tipo = models.CharField(max_length=45, blank=True, default='')
    stock = models.IntegerField(blank=True,null=True)
    imagen = models.ImageField(upload_to='administracion/imagenes',blank=True,null=True)

    #atributos foraneos
    id_producto = models.ForeignKey('self',on_delete=True,null=True,blank=True)

    def __str__(self):
        return self.nombre

class Cotizacion(models.Model):

    #atributos propios
    costo_total = models.FloatField()
    cantidad_productos = models.IntegerField()


class CuentaBancaria(models.Model):

    #atributos propios
    saldo = models.FloatField()

class OrdenDeCompra(models.Model):

    #atributos foraneos
    id_cuenta_bancaria= models.ForeignKey(CuentaBancaria, on_delete=models.CASCADE)
    id_cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    #atributos propios
    nombre_recepcionista = models.CharField(max_length=45, blank=True, default='')
    fecha = models.DateField(auto_now_add=True)
    direccion = models.CharField(max_length=45, blank=True, default='')
    distrito = models.CharField(max_length=45, blank=True, default='')
    provincia= models.CharField(max_length=45, blank=True, default='')
    departamento = models.CharField(max_length=45, blank=True, default='')
    nombre_comprador= models.CharField(max_length=45, blank=True, default='')

