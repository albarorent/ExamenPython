from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from .views import (
    home,
    documentoList,
    documentoCreate,
    documentoUpdate,
    documentoDelete,
    seguroCreate,
    seguroList,
    seguroUpdate,
    seguroDelete,
    pacienteList,
    pacienteCreate,
    pacienteUpdate,
    pacienteDelete,
    especialidadesList,
    especialidadesCreate,
    especialidadesUpdate,
    especialidadesDelete,
    doctorList,
    doctorCreate,
    doctorUpdate,
    doctorDelete,
    citasList,
    citasCreate,
    citasUpdate,
    citasDelete,
    usuarioList,
    usuarioUpdate,
)


urlpatterns = [
    path("", home, name="home"),
    path("tipodocumento/", documentoList.as_view(), name="tipodocumento"),
    path(
        "tipodocumento/create/", documentoCreate.as_view(), name="tipodocumento-create"
    ),
    path(
        "tipodocumento/update/<int:pk>/",
        documentoUpdate.as_view(),
        name="tipodocumento-update",
    ),
    path(
        "tipodocumento/delete/<int:pk>/",
        documentoDelete.as_view(),
        name="tipodocumento-delete",
    ),
    path("tipoSeguro/", seguroList.as_view(), name="tipoSeguro"),
    path("tipoSeguro/create/", seguroCreate.as_view(), name="tipoSeguro-create"),
    path(
        "tipoSeguro/update/<int:pk>/", seguroUpdate.as_view(), name="tipoSeguro-update"
    ),
    path(
        "tipoSeguro/delete/<int:pk>/", seguroDelete.as_view(), name="tipoSeguro-delete"
    ),
    path("paciente/", pacienteList.as_view(), name="paciente"),
    path("paciente/create/", pacienteCreate.as_view(), name="paciente-create"),
    path("paciente/update/<int:pk>/", pacienteUpdate.as_view(), name="paciente-update"),
    path("paciente/delete/<int:pk>/", pacienteDelete.as_view(), name="paciente-delete"),
    path("especialidades/", especialidadesList.as_view(), name="especialidades"),
    path(
        "especialidades/create/",
        especialidadesCreate.as_view(),
        name="especialidades-create",
    ),
    path(
        "especialidades/update/<int:pk>/",
        especialidadesUpdate.as_view(),
        name="especialidades-update",
    ),
    path(
        "especialidades/delete/<int:pk>/",
        especialidadesDelete.as_view(),
        name="especialidades-delete",
    ),
    path("doctores/", doctorList.as_view(), name="doctores"),
    path("doctores/create/", doctorCreate.as_view(), name="doctores-create"),
    path("doctores/update/<int:pk>/", doctorUpdate.as_view(), name="doctores-update"),
    path("doctores/delete/<int:pk>/", doctorDelete.as_view(), name="doctores-delete"),
    path("citas/", citasList.as_view(), name="citas"),
    path("citas/create/", citasCreate.as_view(), name="citas-create"),
    path("citas/update/<int:pk>/", citasUpdate.as_view(), name="citas-update"),
    path("citas/delete/<int:pk>/", citasDelete.as_view(), name="citas-delete"),
    path("usuario/", usuarioList.as_view(), name="usuario"),
    path("usuario/update/<int:pk>/", usuarioUpdate.as_view(), name="usuario-update"),

]
