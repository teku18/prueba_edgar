from django.views.generic import TemplateView, CreateView, UpdateView, ListView
from .models import producto

# Create your views here.

class index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(index,self).get_context_data(**kwargs)
        context['prueba']='prueba'
        return context


class registrar_producto(CreateView):
    model = producto
    template_name = 'registro_productos.html'

#REDIRECCIONA A LA MISMA PAGINA EN LA QUE ESTA PACICIONADO
    def get_success_url(self):
        return self.request.path

    fields = ('nombre', 'descripcion',)


class actualizar_producto(UpdateView):
    model = producto
    template_name = 'actualizar_producto.html'
    success_url = '/productos/registrarProducto'

    fields = ('nombre', 'descripcion',)

class lista_productos(ListView):
    template_name = 'lista_productos.html'
    model = producto
    context_object_name = 'lista_productos'

    def get_context_data(self, **kwargs):
        context = super(lista_productos, self).get_context_data(**kwargs)
        return context