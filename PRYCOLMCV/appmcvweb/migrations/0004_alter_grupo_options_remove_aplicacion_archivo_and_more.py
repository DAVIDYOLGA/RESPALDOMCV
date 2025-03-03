# Generated by Django 5.0.7 on 2025-02-25 18:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmcvweb', '0003_aplicacion_presentacion_actividad_comunicado_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grupo',
            options={'ordering': ['nombre'], 'verbose_name': 'Sede-Area', 'verbose_name_plural': 'SEDES-AREAS'},
        ),
        migrations.RemoveField(
            model_name='aplicacion',
            name='archivo',
        ),
        migrations.AlterField(
            model_name='actividad',
            name='archivo',
            field=models.FileField(default=django.utils.timezone.now, upload_to='media/actividades'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aplicacion',
            name='titulo',
            field=models.CharField(max_length=75, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='comunicado',
            name='titulo',
            field=models.CharField(max_length=75, verbose_name='Titulo del comunicado'),
        ),
    ]
