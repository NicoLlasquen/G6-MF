# Generated by Django 4.2 on 2023-07-05 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion3', '0005_tematica_remove_foro_imagen_remove_foro_usuarioforo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Algebra',
            fields=[
                ('tematica_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aplicacion3.tematica')),
                ('documentos', models.FileField(storage='static/documentos/algebra', upload_to='')),
            ],
            bases=('aplicacion3.tematica',),
        ),
        migrations.CreateModel(
            name='Geometria',
            fields=[
                ('tematica_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aplicacion3.tematica')),
                ('documentos', models.FileField(storage='static/documentos/geometria', upload_to='')),
            ],
            bases=('aplicacion3.tematica',),
        ),
        migrations.CreateModel(
            name='Numeros',
            fields=[
                ('tematica_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aplicacion3.tematica')),
                ('documentos', models.FileField(storage='static/documentos/numeros', upload_to='')),
            ],
            bases=('aplicacion3.tematica',),
        ),
        migrations.CreateModel(
            name='Probabilidad',
            fields=[
                ('tematica_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aplicacion3.tematica')),
                ('documentos', models.FileField(storage='static/documentos/probabilidad', upload_to='')),
            ],
            bases=('aplicacion3.tematica',),
        ),
        migrations.RenameModel(
            old_name='Comentarios',
            new_name='Sugerencias',
        ),
        migrations.DeleteModel(
            name='Foro',
        ),
        migrations.AlterField(
            model_name='tematica',
            name='imagen',
            field=models.ImageField(upload_to='static/imagenes/foro'),
        ),
    ]
