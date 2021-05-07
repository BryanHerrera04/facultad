# Generated by Django 2.2.4 on 2021-05-07 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facu', '0005_auto_20210507_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignatura',
            name='docente',
            field=models.ForeignKey(default='', help_text='Docente', on_delete=django.db.models.deletion.CASCADE, to='facu.Docente', verbose_name='Docente'),
        ),
        migrations.AlterField(
            model_name='docente',
            name='facultad',
            field=models.ForeignKey(default='', help_text='Facultad', on_delete=django.db.models.deletion.CASCADE, to='facu.Facultad', verbose_name='Facultad'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='asignatura',
            field=models.ForeignKey(default='', help_text='Asignatura', on_delete=django.db.models.deletion.CASCADE, to='facu.Asignatura', verbose_name='Asignatura'),
        ),
        migrations.AlterField(
            model_name='facultad',
            name='decano',
            field=models.OneToOneField(default='', help_text='Decano', on_delete=django.db.models.deletion.CASCADE, to='facu.Decano', verbose_name='Decano'),
        ),
    ]
