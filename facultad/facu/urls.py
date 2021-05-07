from django.urls import path, re_path
from facu import views

urlpatterns = [
    re_path(r'^api/decano$', views.decano_list),
    re_path(r'^api/decano/(?P<pk>[0-9]+)$', views.decano_detail),
    re_path(r'^api/facultad$', views.facultad_list),
    re_path(r'^api/facultad/(?P<pk>[0-9]+)$', views.facultad_detail),
    re_path(r'^api/docente$', views.docente_list),
    re_path(r'^api/docente/(?P<pk>[0-9]+)$', views.docente_detail),
    re_path(r'^api/asignatura$', views.asignatura_list),
    re_path(r'^api/asignatura/(?P<pk>[0-9]+)$', views.asignatura_detail),
    re_path(r'^api/estudiante$', views.estudiante_list),
    re_path(r'^api/estudiante/(?P<pk>[0-9]+)$', views.estudiante_detail),
]
