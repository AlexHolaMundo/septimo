# Generated by Django 4.2.6 on 2024-01-09 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Facturacion', '0004_cliente_fotografia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fotografia',
            field=models.FileField(blank=True, null=True, upload_to='clientes'),
        ),
    ]
