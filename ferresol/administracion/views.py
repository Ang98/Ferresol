from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def Principal(request):

    return render(request,'index.html')

def Prueba(request):

    return render(request,'prueba.html')

def RealizarPago(request):

    return render(request,'realizarPago.html')

def CategoriaView(request):

    productos = Producto.objects.filter(tipo = 'Categoria')
    titulo = 'CATEGORIAS'
    link = 'subcategoria'
    carros = CarroProducto(request,request.session['cliente'])

    if not request.session.has_key('cliente'):
        pass
        #carro = Carro.objects.filter(id= )

    else:
        pass

    return render(request,
                  'administracion/categoria.html',
                  context={
                      'productos':productos,
                      'titulo':titulo,
                      'link':link,
                      'carros':carros,
                  })



def SubcategoriaView(request,id):

    productos = Producto.objects.filter(id_producto = id)
    titulo = 'SUBCATEGORIAS'
    link = 'producto'
    carros = CarroProducto(request,request.session['cliente'])

    return render(request,
                  'administracion/categoria.html',
                  context={
                      'productos': productos,
                      'titulo': titulo,
                      'link': link,
                      'carros':carros,
                  })

def ProductoView(request,id):


    productos = Producto.objects.filter(id_producto=id)
    titulo = 'PRODUCTOS'
    padre = id
    link = 'producto'
    carros = CarroProducto(request,request.session['cliente'])

    if request.method=='POST':

        id_p = request.POST['id_producto']
        cant = int(request.POST['cantidad'])

        if not request.session.has_key('cliente'):

            pro = Producto.objects.get(id=id_p)

            costo = cant * pro.precio

            coti = Cotizacion(cantidad_productos=cant,costo_total=costo)
            coti.save()

            coti2=Cotizacion.objects.last()
            request.session['cliente'] = coti2.pk
            car = Carro(id_producto=pro,id_cotizacion= coti2,cantidad=cant)


            car.save()

        else:
            pro = Producto.objects.get(id=id_p)
            costo = cant * pro.precio
            id_coti = request.session['cliente']
            coti = Cotizacion.objects.get(id= id_coti)

            coti.cantidad_productos = cant + coti.cantidad_productos

            coti.costo_total= costo + coti.costo_total

            coti.save()

            car = Carro(id_producto=pro,id_cotizacion= coti,cantidad=cant)
            car.save()

        return render(request,'administracion/categoria.html',context={
                      'productos': productos,
                      'titulo': titulo,
                      'link': link,
                      'padre': padre,
                      'carros':carros,

                  })

    return render(request,
                  'administracion/categoria.html',
                  context={
                      'productos': productos,
                      'titulo': titulo,
                      'link': link,
                      'padre': padre,
                      'carros':carros,
                })




def CarroProducto(request,id):

    if not request.session.has_key('cliente'):
        carro = Carro.objects.filter(id_cotizacion = id)
    else:
        carro = []


    return carro


