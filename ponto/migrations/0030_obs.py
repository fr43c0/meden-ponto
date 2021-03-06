# Generated by Django 2.1.5 on 2019-02-25 21:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ponto', '0029_entraram_display'),
    ]

    operations = [
        migrations.CreateModel(
            name='Obs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrada', models.DateTimeField(blank=True, null=True)),
                ('saida', models.DateTimeField(blank=True, null=True)),
                ('observacoes', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('display', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('colaborador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='observou', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Obs',
            },
        ),
    ]
