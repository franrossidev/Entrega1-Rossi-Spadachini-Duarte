# Generated by Django 4.0.6 on 2022-07-27 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_masdatosusuario_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masdatosusuario',
            name='link_pagina',
            field=models.URLField(blank=True, null=True),
        ),
    ]
