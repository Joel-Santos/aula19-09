from django.db import models

class Music(models.Model):
    titulo  = models.CharField(max_length=50)
    artista = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    data = models.DateField()

    def __str__(self):
        return self.titulo
