# Generated by Django 2.1.5 on 2019-02-12 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ponto', '0014_remove_periodo_jornada_trab'),
    ]

    operations = [
        migrations.AddField(
            model_name='periodo',
            name='jornada_h',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='periodo',
            name='jornada_m',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='periodo',
            name='jornada_s',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
