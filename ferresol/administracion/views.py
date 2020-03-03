from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def Principal(request):

    return render(request,'index.html')

def Prueba(request):

    return render(request,'prueba.html')

def RealizarPago(request):

    carros = CarroProducto(request)

    if request.method=='POST':
        nt = request.POST['nt']
        if request.POST['cv']=='':
            cv= 0
        else:
            cv = int(request.POST['cv'])
        fv= request.POST['fv']

        valor = VerificarUsuario(nt,cv,fv)
        if valor:

            cuenta = CuentaBancaria.objects.get(numero_tarjeta=nt, cv=cv, fecha_vencimiento=fv)
            coti = Cotizacion.objects.get(id=request.session['cliente'])

            orden= OrdenDeCompra(id_cotizacion=coti,id_cuenta_bancaria=cuenta)
            orden.save()

            del request.session['cliente']

            return redirect('principal')
        else:
            return render(request,'realizarPago.html',{'error':'Informacion de tarjeta no valida'})



    return render(request,'realizarPago.html',
                  context={
                      'carros': carros,
                  })


def DatosEmpresa(request):

    return render(request,'datosEmpresa.html')

def CategoriaView(request):

    productos = Producto.objects.filter(tipo = 'Categoria')
    titulo = 'CATEGORIAS'
    link = 'subcategoria'
    carros = CarroProducto(request)

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
    carros = CarroProducto(request)

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
            car = Carro(id_producto=pro,id_cotizacion= coti2,cantidad=cant,subtotal= costo)


            car.save()

        else:
            pro = Producto.objects.get(id=id_p)
            costo = cant * pro.precio
            id_coti = request.session['cliente']
            coti = Cotizacion.objects.get(id= id_coti)

            coti.cantidad_productos = cant + coti.cantidad_productos

            coti.costo_total= costo + coti.costo_total

            coti.save()

            car = Carro(id_producto=pro,id_cotizacion= coti,cantidad=cant,subtotal= costo)
            car.save()

        carros = CarroProducto(request)
        return render(request,'administracion/categoria.html',context={
                      'productos': productos,
                      'titulo': titulo,
                      'link': link,
                      'padre': padre,
                      'carros':carros,

                  })
    carros = CarroProducto(request)
    return render(request,
                  'administracion/categoria.html',
                  context={
                      'productos': productos,
                      'titulo': titulo,
                      'link': link,
                      'padre': padre,
                      'carros':carros,
                })




def CarroProducto(request):

    if request.session.has_key('cliente'):
        carro = Carro.objects.filter(id_cotizacion = request.session['cliente'])
    else:
        carro = []


    return carro

def VerificarUsuario(nt,cv,fv):


    try:
        car = CuentaBancaria.objects.get(numero_tarjeta=nt,cv=cv,fecha_vencimiento=fv)
        valor =True
    except CuentaBancaria.DoesNotExist:
        valor = False

    return valor

