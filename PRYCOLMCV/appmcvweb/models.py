from django.db import models
from django.core.validators import URLValidator
from datetime import datetime

# Create your models here.
class grupo(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Area Encargada')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ('Sede-Area')
        verbose_name_plural = ('SEDES-AREAS')
        ordering = ['nombre']
    def __str__(self):
        return self.nombre

tipfile = [
    ["MP4", "Video"],
    ["JPG", "Foto-Imagen"],
    ["MP3", "Musica-Sonido"],
    ["PDF", "Documento Pdf"],
]

class inicio(models.Model):
    titulo=models.CharField(max_length=50,verbose_name='Nombre' )
    grupo = models.ForeignKey(grupo, on_delete=models.CASCADE, verbose_name='Area Encargada')
    contenido = models.TextField()
    archivo = models.FileField(upload_to='media/inicio')
    tipo = models.CharField(max_length=3,choices=tipfile)
    enlace = models.TextField(validators=[URLValidator()], null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = ('Bienvenida')
        verbose_name_plural = ('Bienvenidas')
        ordering = ['-updated']
    def __str__(self): 
        return self.titulo
  


# Create your models here.
class presentacion(models.Model):
    titulo=models.CharField(max_length=50,verbose_name='Nombre' )
    imagen = models.ImageField(upload_to='media/presentacion' )
    archivo = models.FileField(upload_to='media/presentacion', null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name:'Presentacion'
        verbose_name_plural = ('Presentaciones')

        ordering = ['-updated']
    def __str__(self):
        return self.titulo


 
class publicacion(models.Model):
    titulo=models.CharField(max_length=50,verbose_name='Nombre' )
    grupo=models.ForeignKey(grupo, on_delete=models.CASCADE)
    contenido = models.TextField()
    imagen=models.ImageField(upload_to='media/publicaciones' )
    archivo = models.FileField(upload_to='media/publicaciones', null=True, blank=True )
    autor = models.CharField(max_length=50,verbose_name="Autor")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = ('Publicacion')
        verbose_name_plural = ('Publicaciones')
        ordering = ['-updated']
    def __str__(self):
        return self.titulo

class actividad(models.Model):
    titulo = models.CharField(max_length=50, verbose_name='Nombre de la actividad')
    grupo = models.ForeignKey(grupo, on_delete=models.CASCADE, verbose_name='Area Encargada' )
    fechaact = models.DateField(verbose_name='Fecha del evento')
    contenido = models.TextField( verbose_name='Descripcion del Evento'  )
    imagen = models.ImageField(upload_to='media/actividades' )
    archivo = models.FileField(upload_to='media/actividades')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name= ('Actividad')
        verbose_name_plural= ('Actividades')
        ordering = ['-fechaact']
    def __str__(self):
        return self.titulo

class comunicado(models.Model):
    titulo = models.CharField(max_length=75, verbose_name='Titulo del comunicado')
    grupo = models.ForeignKey(grupo, on_delete=models.CASCADE, verbose_name='Area Encargada')
    fechaact = models.DateField(verbose_name='Fecha')
    archivo = models.FileField(upload_to='media/comunicados')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name= ('comunicado')
        verbose_name_plural= ('comunicados')
        ordering = ['-fechaact']
    def __str__(self):
        return self.titulo


class aplicacion(models.Model):
    titulo=models.CharField(max_length=75,verbose_name='Nombre')
    enlace= models.TextField(validators= [URLValidator()])
    imagen = models.ImageField(upload_to='media/aplicacion')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name= ('Aplicacion')
        verbose_name_plural= ('Aplicaciones')
        ordering = ['-updated']
    def __str__(self):
        return self.titulo