# Generated by Django 2.2.4 on 2021-05-07 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facu', '0004_facultad_decano'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignatura',
            name='cod_asig',
            field=models.CharField(default='', help_text='Código de la Asignatura', max_length=50, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='asignatura',
            name='nom_asig',
            field=models.CharField(default='', help_text='Nombre de la Asignatura', max_length=50, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='asignatura',
            name='num_cred_asig',
            field=models.CharField(default='', help_text='Creditos de la Asignatura', max_length=50, verbose_name='Creditos'),
        ),
        migrations.AlterField(
            model_name='facultad',
            name='decano',
            field=models.OneToOneField(default='', help_text='Decano', on_delete=django.db.models.deletion.DO_NOTHING, to='facu.Decano', verbose_name='Decano'),
        ),
    ]
