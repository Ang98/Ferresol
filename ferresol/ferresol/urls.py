
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from administracion import views as admi_v

urlpatterns = [
    path('admin/', admin.site.urls),

    path('principal/',admi_v.Principal,name='principal'),

    path('categoria/',admi_v.CategoriaView,name='categoria'),

    path('subcategoria/<int:id>',admi_v.SubcategoriaView,name='subcategoria'),

    path('producto/<int:id>',admi_v.ProductoView,name='producto'),

] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
