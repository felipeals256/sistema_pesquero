# Generated by Django 4.0.2 on 2022-08-07 03:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_botehistorico_user_responsable_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sector',
            options={'verbose_name': 'Sector', 'verbose_name_plural': 'Sectores'},
        ),
        migrations.AddField(
            model_name='arte',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='arte',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='arte',
            name='user_creador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='creado por'),
        ),
        migrations.AddField(
            model_name='arte',
            name='user_modificador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='modificado por'),
        ),
        migrations.AddField(
            model_name='botevigencia',
            name='user_creador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='creado por'),
        ),
        migrations.AddField(
            model_name='especie',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='especie',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='especie',
            name='user_creador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='creado por'),
        ),
        migrations.AddField(
            model_name='especie',
            name='user_modificador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='modificado por'),
        ),
        migrations.AddField(
            model_name='especietipo',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='especietipo',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='especietipo',
            name='user_creador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='creado por'),
        ),
        migrations.AddField(
            model_name='especietipo',
            name='user_modificador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='modificado por'),
        ),
        migrations.AddField(
            model_name='isla',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='isla',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='isla',
            name='user_creador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='creado por'),
        ),
        migrations.AddField(
            model_name='isla',
            name='user_modificador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='modificado por'),
        ),
        migrations.AddField(
            model_name='sector',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='sector',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sector',
            name='user_creador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='creado por'),
        ),
        migrations.AddField(
            model_name='sector',
            name='user_modificador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='modificado por'),
        ),
        migrations.AddField(
            model_name='unidad',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='unidad',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unidad',
            name='user_creador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='creado por'),
        ),
        migrations.AddField(
            model_name='unidad',
            name='user_modificador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='modificado por'),
        ),
        migrations.AddField(
            model_name='zona',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='zona',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zona',
            name='user_creador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='creado por'),
        ),
        migrations.AddField(
            model_name='zona',
            name='user_modificador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='modificado por'),
        ),
        migrations.AlterField(
            model_name='arte',
            name='codigo',
            field=models.CharField(max_length=50, unique=True, verbose_name='código'),
        ),
        migrations.AlterField(
            model_name='arte',
            name='descripcion',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='descripción'),
        ),
        migrations.AlterField(
            model_name='bote',
            name='descripcion',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='descripción'),
        ),
        migrations.AlterField(
            model_name='bote',
            name='numero',
            field=models.IntegerField(unique=True, verbose_name='número'),
        ),
        migrations.AlterField(
            model_name='bote',
            name='user_creador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='creado por'),
        ),
        migrations.AlterField(
            model_name='bote',
            name='user_modificador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='modificado por'),
        ),
        migrations.AlterField(
            model_name='botehistorico',
            name='user_modificador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='modificado por'),
        ),
        migrations.AlterField(
            model_name='botevigencia',
            name='user_modificador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='modificado por'),
        ),
        migrations.AlterField(
            model_name='especie',
            name='codigo',
            field=models.CharField(max_length=5, unique=True, verbose_name='código'),
        ),
        migrations.AlterField(
            model_name='especietipo',
            name='codigo',
            field=models.IntegerField(unique=True, verbose_name='código'),
        ),
        migrations.AlterField(
            model_name='isla',
            name='codigo',
            field=models.CharField(max_length=3, unique=True, verbose_name='código'),
        ),
        migrations.AlterField(
            model_name='isla',
            name='descripcion',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='descripción'),
        ),
        migrations.AlterField(
            model_name='sector',
            name='codigo',
            field=models.CharField(max_length=100, unique=True, verbose_name='código'),
        ),
        migrations.AlterField(
            model_name='sector',
            name='descripcion',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='descripción'),
        ),
        migrations.AlterField(
            model_name='unidad',
            name='codigo',
            field=models.IntegerField(unique=True, verbose_name='código'),
        ),
        migrations.AlterField(
            model_name='unidad',
            name='descripcion',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='descripción'),
        ),
        migrations.AlterField(
            model_name='zona',
            name='codigo',
            field=models.IntegerField(unique=True, verbose_name='código'),
        ),
        migrations.AlterField(
            model_name='zona',
            name='descripcion',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='descripción'),
        ),
    ]