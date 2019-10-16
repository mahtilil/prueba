from django.db import models

# Create your models here.


class Pregunta(models.Model):
    descripcion = models.CharField(max_length=200)
    fecha = models.DateTimeField('date published')

    def __str__(self):
        return self.descripcion

    def was_published_recently(self):
        return self.fecha >= timezone.now() - datetime.timedelta(days=1)


class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.descripcion