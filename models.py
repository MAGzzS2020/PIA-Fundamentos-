from django.db import models

# Create your models here.

class Carrera(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=50)
    duracion = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        txt = "{0} (Duracion: {1} años(s))"
        return txt.format(self.nombre,self.duracion)

class Estudiante(models.Model):
    dni = models.CharField(max_length=8, primary_key=True)
    apellidopaterno = models.CharField(max_length=35)
    apellidomaterno = models.CharField(max_length=35)
    nombres = models.CharField(max_length=35)
    fechanacimiento = models.DateField()
    sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    sexo = models.CharField(max_length=1,choices=sexos,default= 'F')
    Carrera = models.ForeignKey(Carrera,null=False,blank=False, on_delete=models.CASCADE)
    Vigencia = models.BooleanField(default= True)

    def __str__(self):
        txt = "{0} {1} {2}"
        return txt.format(self.apellidopaterno, self.apellidomaterno, self.nombres)

class Curso(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveBigIntegerField()
    docente = models.CharField(max_length=100)

    def __str__(self):
        txt = "{0} (creditos: {1})"
        return txt.format(self.nombre,self.creditos)

class Matricula(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    Curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    FechaMatricula = models.DateField(auto_now_add=True)

    def __str__(self):
        txt = "{0} ({1})"
        return txt.format(self.Curso,self.estudiante)
