from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, FormView, DeleteView, DetailView
from .models import producto
from .forms import productosForm
from django.core.urlresolvers import reverse_lazy

# Create your views here.

class index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(index,self).get_context_data(**kwargs)
        context['prueba']='prueba'
        return context


class registrar_producto(FormView):
    # model = producto
    form_class = productosForm
    template_name = 'registro_productos.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        form.save()
        print('se guadro correctamente todo')
        return super(registrar_producto, self).form_valid(form)
#
# #REDIRECCIONA A LA MISMA PAGINA EN LA QUE ESTA POCICIONADO
#     def get_success_url(self):
#         return self.request.path


class actualizar_producto(UpdateView):
    model = producto
    template_name = 'actualizar_producto.html'
    form_class =productosForm
    success_url = '/listaProducto'


class lista_productos(ListView):
    template_name = 'lista_productos.html'
    #model = producto
    context_object_name = 'lista_productos'

    #traigo la lista de los datos con el queryset ya que me permite
    #traer la lista de los datos ordenados
    queryset = producto.objects.all().order_by('id')


    def get_context_data(self, **kwargs):
        context = super(lista_productos, self).get_context_data(**kwargs)
        return context

class eliminar_producto(DeleteView):
    template_name = 'eliminar_producto.html'
    model = producto
    success_url = reverse_lazy('lista-productos')

class detalle_producto(DetailView):
    template_name = 'detalle_producto.html'
    model = producto
    context_object_name = 'detalle_producto'