from django.conf.urls import url
from .views import index, registrar_producto, actualizar_producto, lista_productos

urlpatterns = [

    url(r'^$', index.as_view(), name='inicio'),
    url(r'^registrarProducto/$', registrar_producto.as_view(), name='registrar_producto'),
    url(r'^actualizarProducto/(?P<pk>\d+)', actualizar_producto.as_view(), name='actualizar-producto'),

    url(r'^listaProducto$', lista_productos.as_view(), name='lista-productos'),
]