from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','precio','tipo','stock','imagen','id_producto')
    search_fields = ('nombre','tipo','id')

@admin.register(Cotizacion)
class CotizacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'costo_total', 'cantidad_productos')
    search_fields = ('id','cantidad_productos')

@admin.register(CuentaBancaria)
class CuentaBancariaAdmin(admin.ModelAdmin):
    list_display = ('id', 'saldo')
    search_fields = ('id','saldo')

@admin.register(OrdenDeCompra)
class OrdenDeCompraAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_cuenta_bancaria', 'id_cotizacion', 'id_producto', 'nombre_recepcionista', 'fecha', 'direccion', 'distrito', 'provincia', 'departamento', 'nombre_comprador')
    search_fields = ('id_cuenta_bancaria', 'id_cotizacion', 'id','id_producto')