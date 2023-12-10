# Generated by Django 4.2.7 on 2023-12-10 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cedula', models.CharField(max_length=10)),
                ('apellido', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.TextField(max_length=100)),
                ('fechas_nacimiento', models.DateField()),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
    ]