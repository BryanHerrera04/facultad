from rest_framework import serializers
from facu.models import Decano, Facultad, Docente, Asignatura, Estudiante


class DecanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decano
        fields = ('id', 'nom_decano', 'ape_decano', 'cedula', 'cel_decano',)


class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultad
        fields = ('id', 'nom_facultad', 'num_blo_facultad',
                  'ubi_facultad', 'decano',)


class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = ('id', 'nom_docente', 'ape_docente',
                  'cc_docente', 'titulo_docente', 'facultad')


class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = ('id', 'nom_asig', 'cod_asig', 'num_cred_asig', 'docente', )


class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ('id', 'nom_est', 'ape_est',
                  'cc_est', 'dir_est', 'asignatura')
