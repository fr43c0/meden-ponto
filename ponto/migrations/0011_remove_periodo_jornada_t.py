# Generated by Django 2.1.5 on 2019-02-12 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ponto', '0010_auto_20190212_0026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='periodo',
            name='jornada_t',
        ),
    ]
