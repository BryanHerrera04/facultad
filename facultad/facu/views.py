from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from facu.models import Decano, Facultad, Docente, Asignatura, Estudiante
from facu.serializers import DecanoSerializer, FacultadSerializer, DocenteSerializer, AsignaturaSerializer, EstudianteSerializer

# Create your views here.

# DECANO


@api_view(['GET', 'POST', 'DELETE', ])
def decano_list(request):
    # Recuperar todos los decanos
    if request.method == 'GET':
        nom_decano = request.GET.get('nom_decano', None)

        if nom_decano is not None:
            decanos = Decano.objects.filter(nom_decano__icontains=nom_decano)
        else:
            decanos = Decano.objects.all()

        decanos_serializer = DecanoSerializer(decanos, many=True)
        return JsonResponse(decanos_serializer.data, safe=False)

    # Crear y guardar un decano nuevo
    elif request.method == 'POST':
        decano_datos = JSONParser().parse(request)
        decano_serializer = DecanoSerializer(data=decano_datos)

        if decano_serializer.is_valid():
            decano_serializer.save()
            return JsonResponse(decano_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(decano_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Eliminar todos los decanos
    elif request.method == 'DELETE':
        conteo = Decano.objects.all().delete()

        return JsonResponse(
            {
                'message': '{} Decanos fueron eliminados exitosamente'. format(conteo[0])
            },
            status=status.HTTP_204_NO_CONTENT
        )


@api_view(['GET', 'PUT', 'DELETE', ])
def decano_detail(request, pk):
    try:
        decano = Decano.objects.get(pk=pk)
    except Decano.DoesNotExist:
        return JsonResponse({
            'message': 'El decano no existe'
        }, status=status.HTTP_404_NOT_FOUND)

    # Recuperar un decano por un id
    if request.method == 'GET':
        decano_serializer = DecanoSerializer(decano)
        return JsonResponse(decano_serializer.data)

    # Actualizar un decano por el id
    elif request.method == 'PUT':
        decano_datos = JSONParser().parse(request)
        decano_serializer = DecanoSerializer(decano, data=decano_datos)

        if decano_serializer.is_valid():
            decano_serializer.save()
            return JsonResponse(decano_serializer.data)
        return JsonResponse(decano_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Eliminna un decano por el id
    elif request.method == 'DELETE':
        decano.delete()
        return JsonResponse(
            {'message': 'El decano fue elimiado exitosamennte'},
            status=status.HTTP_204_NO_CONTENT)


# FACULTAD
@api_view(['GET', 'POST', 'DELETE', ])
def facultad_list(request):
    # Recuperar todos los facultades
    if request.method == 'GET':
        nom_facultad = request.GET.get('nom_facultad', None)

        if nom_facultad is not None:
            facultads = Facultad.objects.filter(
                nom_facultad__icontains=nom_facultad)
        else:
            facultads = Facultad.objects.all()

        facultads_serializer = FacultadSerializer(facultads, many=True)
        return JsonResponse(facultads_serializer.data, safe=False)

    # Crear y guardar un facultad nuevo
    elif request.method == 'POST':
        facultad_datos = JSONParser().parse(request)
        facultad_serializer = FacultadSerializer(data=facultad_datos)

        if facultad_serializer.is_valid():
            facultad_serializer.save()
            return JsonResponse(facultad_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(facultad_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Eliminar todos los facultads
    elif request.method == 'DELETE':
        conteo = Facultad.objects.all().delete()

        return JsonResponse(
            {
                'message': '{} Facultades fueron eliminados exitosamente'. format(conteo[0])
            },
            status=status.HTTP_204_NO_CONTENT
        )


@api_view(['GET', 'PUT', 'DELETE', ])
def facultad_detail(request, pk):
    try:
        facultad = Facultad.objects.get(pk=pk)
    except Facultad.DoesNotExist:
        return JsonResponse({
            'message': 'El facultad no existe'
        }, status=status.HTTP_404_NOT_FOUND)

    # Recuperar un facultad por un id
    if request.method == 'GET':
        facultad_serializer = FacultadSerializer(facultad)
        return JsonResponse(facultad_serializer.data)

    # Actualizar un facultad por el id
    elif request.method == 'PUT':
        facultad_datos = JSONParser().parse(request)
        facultad_serializer = FacultadSerializer(facultad, data=facultad_datos)

        if facultad_serializer.is_valid():
            facultad_serializer.save()
            return JsonResponse(facultad_serializer.data)
        return JsonResponse(facultad_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Elimina un facultad por el id
    elif request.method == 'DELETE':
        facultad.delete()
        return JsonResponse(
            {'message': 'La facultad fue elimiado exitosamennte'},
            status=status.HTTP_204_NO_CONTENT)


# DOCENTE
@api_view(['GET', 'POST', 'DELETE', ])
def docente_list(request):
    # Recuperar todos los docentes
    if request.method == 'GET':
        nom_docente = request.GET.get('nom_docente', None)

        if nom_docente is not None:
            docentes = Docente.objects.filter(
                nom_docente__icontains=nom_docente)
        else:
            docentes = Docente.objects.all()

        docentes_serializer = DocenteSerializer(docentes, many=True)
        return JsonResponse(docentes_serializer.data, safe=False)

    # Crear y guardar un docente nuevo
    elif request.method == 'POST':
        docente_datos = JSONParser().parse(request)
        docente_serializer = DocenteSerializer(data=docente_datos)

        if docente_serializer.is_valid():
            docente_serializer.save()
            return JsonResponse(docente_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(docente_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Eliminar todos los docentes
    elif request.method == 'DELETE':
        conteo = Docente.objects.all().delete()

        return JsonResponse(
            {
                'message': '{} Docentes fueron eliminados exitosamente'. format(conteo[0])
            },
            status=status.HTTP_204_NO_CONTENT
        )


@api_view(['GET', 'PUT', 'DELETE', ])
def docente_detail(request, pk):
    try:
        docente = Docente.objects.get(pk=pk)
    except Docente.DoesNotExist:
        return JsonResponse({
            'message': 'El docente no existe'
        }, status=status.HTTP_404_NOT_FOUND)

    # Recuperar un docente por un id
    if request.method == 'GET':
        docente_serializer = DocenteSerializer(docente)
        return JsonResponse(docente_serializer.data)

    # Actualizar un docente por el id
    elif request.method == 'PUT':
        docente_datos = JSONParser().parse(request)
        docente_serializer = DocenteSerializer(docente, data=docente_datos)

        if docente_serializer.is_valid():
            docente_serializer.save()
            return JsonResponse(docente_serializer.data)
        return JsonResponse(docente_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Eliminna un docente por el id
    elif request.method == 'DELETE':
        docente.delete()
        return JsonResponse(
            {'message': 'El docente fue elimiado exitosamennte'},
            status=status.HTTP_204_NO_CONTENT)

# ASIGNATURA


@api_view(['GET', 'POST', 'DELETE', ])
def asignatura_list(request):
    # Recuperar todos los asignaturas
    if request.method == 'GET':
        nom_asig = request.GET.get('nom_asig', None)

        if nom_asig is not None:
            asignaturas = Asignatura.objects.filter(
                nom_asig__icontains=nom_asig)
        else:
            asignaturas = Asignatura.objects.all()

        asignaturas_serializer = AsignaturaSerializer(asignaturas, many=True)
        return JsonResponse(asignaturas_serializer.data, safe=False)

    # Crear y guardar un asignatura nuevo
    elif request.method == 'POST':
        asignatura_datos = JSONParser().parse(request)
        asignatura_serializer = AsignaturaSerializer(data=asignatura_datos)

        if asignatura_serializer.is_valid():
            asignatura_serializer.save()
            return JsonResponse(asignatura_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(asignatura_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Eliminar todos los asignaturas
    elif request.method == 'DELETE':
        conteo = Asignatura.objects.all().delete()

        return JsonResponse(
            {
                'message': '{} Asignaturas fueron eliminados exitosamente'. format(conteo[0])
            },
            status=status.HTTP_204_NO_CONTENT
        )


@api_view(['GET', 'PUT', 'DELETE', ])
def asignatura_detail(request, pk):
    try:
        asignatura = Asignatura.objects.get(pk=pk)
    except Asignatura.DoesNotExist:
        return JsonResponse({
            'message': 'El asignatura no existe'
        }, status=status.HTTP_404_NOT_FOUND)

    # Recuperar un asignatura por un id
    if request.method == 'GET':
        asignatura_serializer = AsignaturaSerializer(asignatura)
        return JsonResponse(asignatura_serializer.data)

    # Actualizar un asignatura por el id
    elif request.method == 'PUT':
        asignatura_datos = JSONParser().parse(request)
        asignatura_serializer = AsignaturaSerializer(
            asignatura, data=asignatura_datos)

        if asignatura_serializer.is_valid():
            asignatura_serializer.save()
            return JsonResponse(asignatura_serializer.data)
        return JsonResponse(asignatura_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Eliminna un asignatura por el id
    elif request.method == 'DELETE':
        asignatura.delete()
        return JsonResponse(
            {'message': 'La asignatura fue elimiado exitosamennte'},
            status=status.HTTP_204_NO_CONTENT)

# ESTUDIANTE


@api_view(['GET', 'POST', 'DELETE', ])
def estudiante_list(request):
    # Recuperar todos los estudiantes
    if request.method == 'GET':
        nom_est = request.GET.get('nom_est', None)

        if nom_est is not None:
            estudiantes = Estudiante.objects.filter(nom_est__icontains=nom_est)
        else:
            estudiantes = Estudiante.objects.all()

        estudiantes_serializer = EstudianteSerializer(estudiantes, many=True)
        return JsonResponse(estudiantes_serializer.data, safe=False)

    # Crear y guardar un estudiante nuevo
    elif request.method == 'POST':
        estudiante_datos = JSONParser().parse(request)
        estudiante_serializer = EstudianteSerializer(data=estudiante_datos)

        if estudiante_serializer.is_valid():
            estudiante_serializer.save()
            return JsonResponse(estudiante_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(estudiante_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Eliminar todos los estudiantes
    elif request.method == 'DELETE':
        conteo = Estudiante.objects.all().delete()

        return JsonResponse(
            {
                'message': '{} Estudiantes fueron eliminados exitosamente'. format(conteo[0])
            },
            status=status.HTTP_204_NO_CONTENT
        )


@api_view(['GET', 'PUT', 'DELETE', ])
def estudiante_detail(request, pk):
    try:
        estudiante = Estudiante.objects.get(pk=pk)
    except Estudiante.DoesNotExist:
        return JsonResponse({
            'message': 'El estudiante no existe'
        }, status=status.HTTP_404_NOT_FOUND)

    # Recuperar un estudiante por un id
    if request.method == 'GET':
        estudiante_serializer = EstudianteSerializer(estudiante)
        return JsonResponse(estudiante_serializer.data)

    # Actualizar un estudiante por el id
    elif request.method == 'PUT':
        estudiante_datos = JSONParser().parse(request)
        estudiante_serializer = EstudianteSerializer(
            estudiante, data=estudiante_datos)

        if estudiante_serializer.is_valid():
            estudiante_serializer.save()
            return JsonResponse(estudiante_serializer.data)
        return JsonResponse(estudiante_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Eliminna un estudiante por el id
    elif request.method == 'DELETE':
        estudiante.delete()
        return JsonResponse(
            {'message': 'El estudiante fue elimiado exitosamennte'},
            status=status.HTTP_204_NO_CONTENT)
