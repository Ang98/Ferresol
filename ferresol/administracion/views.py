from django.shortcuts import render
from .models import *
# Create your views here.



def Principal(request):

    return render(request,'index.html')

def Prueba(request):

    return render(request,'prueba.html')



def CategoriaView(request):

    productos = Producto.objects.filter(tipo = 'Categoria')
    titulo = 'CATEGORIAS'
    link = 'subcategoria'
    return render(request,
                  'administracion/categoria.html',
                  context={
                      'productos':productos,
                      'titulo':titulo,
                      'link':link,
                  })



def SubcategoriaView(request,id):

    productos = Producto.objects.filter(id_producto = id)
    titulo = 'SUBCATEGORIAS'
    link = 'producto'

    return render(request,
                  'administracion/categoria.html',
                  context={
                      'productos': productos,
                      'titulo': titulo,
                      'link': link,
                  })

def ProductoView(request,id):
    productos = Producto.objects.filter(id_producto=id)
    titulo = 'PRODUCTOS'

    link = 'producto'

    return render(request,
                  'administracion/categoria.html',
                  context={
                      'productos': productos,
                      'titulo': titulo,
                      'link': link,
                  })