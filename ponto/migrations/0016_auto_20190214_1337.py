# Generated by Django 2.1.5 on 2019-02-14 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ponto', '0015_auto_20190212_0102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='periodo',
            name='jornada_h',
        ),
        migrations.RemoveField(
            model_name='periodo',
            name='jornada_m',
        ),
        migrations.RemoveField(
            model_name='periodo',
            name='jornada_s',
        ),
    ]
