from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
    path('', views.Inicio.as_view(), name="Inicio"),
    path('Publicaciones', views.Publicaciones, name="Publicaciones"),
    path('Actividades', views.Actividades, name="Actividades"),
    path('Institucional', views.Institucional, name="Institucional"),
    path('Comunicados', views.Comunicados, name="Comunicados"),
    path('Aplicaciones', views.Aplicaciones, name="Aplicaciones"),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)