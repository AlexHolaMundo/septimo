# Generated by Django 4.2.6 on 2024-01-09 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Facturacion', '0003_rename_tipocliente_tipo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='fotografia',
            field=models.ImageField(blank=True, null=True, upload_to='clientes'),
        ),
    ]
