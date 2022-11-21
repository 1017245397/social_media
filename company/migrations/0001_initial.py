# Generated by Django 4.1.3 on 2022-11-20 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit', models.CharField(max_length=20, unique=True, verbose_name='nit')),
                ('description', models.TextField(blank=True, verbose_name='descripcion')),
                ('mision', models.TextField(blank=True, verbose_name='mision')),
                ('vision', models.TextField(blank=True, verbose_name='vision')),
                ('name', models.CharField(max_length=50, verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'empresa',
                'verbose_name_plural': 'empresas',
            },
        ),
    ]