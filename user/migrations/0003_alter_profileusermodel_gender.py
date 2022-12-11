# Generated by Django 4.1.3 on 2022-12-11 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_profileuser_profileusermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileusermodel',
            name='gender',
            field=models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino'), ('OTHER', 'Otros')], max_length=10, verbose_name='Genero'),
        ),
    ]
