# Generated by Django 3.2.9 on 2021-11-11 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0002_empleado_matricula'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='apellido_Materno',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='empleado',
            name='apellido_Paterno',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='nombre',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='rfc',
            field=models.CharField(default='', max_length=50),
        ),
    ]
