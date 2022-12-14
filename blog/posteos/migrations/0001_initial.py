# Generated by Django 4.1 on 2022-10-01 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Posteo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, unique=True)),
                ('subtitulo', models.CharField(max_length=200, unique=True)),
                ('actualizado', models.DateTimeField()),
                ('contenido', models.TextField()),
                ('creado', models.DateTimeField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['creado'],
            },
        ),
    ]
