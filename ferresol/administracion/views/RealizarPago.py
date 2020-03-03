from django.shortcuts import render, redirect
from ..models import *
from .Categoria import CarroProducto

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

def VerificarUsuario(nt,cv,fv):


    try:
        car = CuentaBancaria.objects.get(numero_tarjeta=nt,cv=cv,fecha_vencimiento=fv)
        valor =True
    except CuentaBancaria.DoesNotExist:
        valor = False

    return valor
