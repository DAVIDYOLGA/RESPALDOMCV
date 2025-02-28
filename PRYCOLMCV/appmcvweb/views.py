from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.base import TemplateView

from django.http import HttpResponse, JsonResponse

from .models import inicio
from .models import presentacion
from .models import publicacion
from .models import actividad
from .models import comunicado
from .models import aplicacion


# para tomar en cuenta en la ordenacion y filtro de datos
# internamientos = Internamiento.objects.order_by('Cuarto').filter(
#    Q(fecha_egreso__gt=datetime.now()) | Q(fecha_egreso__isnull=True)
# )

# Create your views here.

class Inicio(TemplateView):
    template_name = 'appmcvweb/inicio.html'
    def get_context_data(self, *args, **kwargs):
        inicios = inicio.objects.all()
        return {'inicios': inicios,}
    

def Publicaciones(request):
    publicaciones = publicacion.objects.all()
    return render(request, 'appmcvweb/Publicaciones.html', {"publicaciones": publicaciones})

def Actividades(request):
    actividades = actividad.objects.all()
    return render(request, "appmcvweb/Actividades.html", {"actividades": actividades})

def Institucional(request):
    presentaciones = presentacion.objects.all()
    return render(request, "appmcvweb/Institucional.html", {"presentaciones": presentaciones})

def Comunicados(request):
    comunicados = comunicado.objects.all()
    return render(request, "appmcvweb/Comunicados.html", {"comunicados": comunicados})

def Aplicaciones(request):
    aplicaciones = aplicacion.objects.all()
    return render(request, 'appmcvweb/Aplicaciones.html', {"aplicaciones": aplicaciones})