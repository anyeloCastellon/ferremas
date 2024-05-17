from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from .models import Contacto
from .serializers import ContactoSerializer



from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import ContactoForm


class ContactoCreateAPIView(CreateAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer



class ContactoCreateView(CreateView):
    model = Contacto
    form_class = ContactoForm
    template_name = 'contacto_form.html'
    success_url = reverse_lazy('contacto_success')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user if self.request.user.is_authenticated else None
        return kwargs

    def form_valid(self, form):
        form.instance.usuario = self.request.user if self.request.user.is_authenticated else None
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigation'] = [
            {'name': 'Inicio', 'route': '/'},
            {'name': 'Productos', 'route': '/productos'},
            {'name': 'Quienes Somos', 'route': '/quienes-somos'},
            {'name': 'Contacto', 'route': '/contacto'},
        ]
        return context