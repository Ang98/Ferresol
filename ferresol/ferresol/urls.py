
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from administracion import views as admi_v

urlpatterns = [
    path('admin/', admin.site.urls),

    path('principal/',admi_v.Principal,name='principal'),

    path('prueba/',admi_v.Prueba,name='prueba'),

    path('categoria/',admi_v.CategoriaView,name='categoria'),
    
    
    path('realizarPago/',admi_v.RealizarPago,name='realizarPago'),

    path('datosEmpresa/',admi_v.DatosEmpresa,name='datosEmpresa'),

    path('subcategoria/<int:id>',admi_v.SubcategoriaView,name='subcategoria'),

    path('producto/<int:id>',admi_v.ProductoView,name='producto'),

] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
