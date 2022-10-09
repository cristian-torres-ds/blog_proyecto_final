# Generated by Django 4.1 on 2022-10-04 18:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mensajes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mensaje',
            options={'ordering': ['creado']},
        ),
        migrations.RemoveField(
            model_name='mensaje',
            name='mensaje',
        ),
        migrations.AddField(
            model_name='mensaje',
            name='contenido',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mensaje',
            name='creado',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='emisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='receptor',
            field=models.IntegerField(),
        ),
    ]