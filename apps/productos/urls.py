from django.conf.urls import url
from .views import index, registrar_producto, actualizar_producto, lista_productos, eliminar_producto, detalle_producto

urlpatterns = [

    url(r'^$', index.as_view(), name='inicio'),
    url(r'^registrarProducto/$', registrar_producto.as_view(), name='registrar_producto'),
    url(r'^actualizarProducto/(?P<pk>\d+)', actualizar_producto.as_view(), name='actualizar-producto'),

    url(r'^listaProducto$', lista_productos.as_view(), name='lista-productos'),

    url(r'^eliminarProducto/(?P<pk>\d+)', eliminar_producto.as_view(), name='eliminar-producto'),

    url(r'^detalleProducto/(?P<pk>\d+)', detalle_producto.as_view(), name='detalle-producto'),
]