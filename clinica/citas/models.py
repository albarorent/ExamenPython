from django.db import models

from users.models import usuario

# Create your models here.



class tipoDocumento(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = "tipodocumento"
        # ordering = ["completed"]
        
class tipoSeguro(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = "tipoSeguro"
        # ordering = ["completed"]
        
class Doctores(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=50)

    class Meta:
        db_table = "doctores"
        # ordering = ["completed"]

class Especialidades(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = "especialidades"
        # ordering = ["completed"]

class Paciente(models.Model):
    tipodocumento = models.ForeignKey(tipoDocumento, on_delete=models.CASCADE,null=True,blank=True)
    nDocumento = models.CharField(max_length=20)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=200)
    direccion = models.CharField(max_length=150,null=True)
    fechaNacimiento = models.DateField()
    tiposeguro = models.ForeignKey(tipoSeguro, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "paciente"
        # ordering = ["completed"]


        
class Citas(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,null=True,blank=True)
    observaciones = models.TextField(null=True, blank=True)
    fechaCita = models.DateField()
    especialidad = models.ForeignKey(Especialidades, on_delete=models.CASCADE, null=True, blank=True)
    doctor = models.ForeignKey(Doctores, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(usuario, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "citas"
        # ordering = ["completed"]