from django.db import models

# Create your models here.


class Animal(models.Model):
    nome_animal = models.CharField(max_length=30)
    predador = models.CharField(max_length=3)
    venenoso = models.CharField(max_length=3)
    domestico = models.CharField(max_length=3)

    def __str__(self):
        return self.nome_animal
