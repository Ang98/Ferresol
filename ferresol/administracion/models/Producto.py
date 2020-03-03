from django.db import models

class Producto(models.Model):

    #atributos propios
    nombre = models.CharField(max_length=45, blank=True, default='')
    precio = models.IntegerField(blank=True,null=True)
    tipo = models.CharField(max_length=45, blank=True, default='')
    stock = models.IntegerField(blank=True,null=True)
    imagen = models.ImageField(upload_to='administracion/imagenes',blank=True,null=True)

    #atributos foraneos
    id_producto = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.nombre