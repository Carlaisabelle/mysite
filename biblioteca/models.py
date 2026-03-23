from django.db import models

class Libro(models.Model):
    titolo = models.CharField(max_length=200)
    autore = models.CharField(max_length=100)
    anno = models.PositiveIntegerField()
    genere = models.CharField(max_length=100, null=True, blank=True)
    lingua_og = models.CharField(max_length=50, null=True, blank=True)

    # __str__: definisce come la classe viene mostrata a display
    def __str__(self):
        return f'"{self.titolo}", scritto da {self.autore}'
    
class Autore(models.Model):
    nome_completo = models.CharField(max_length=200)
    nome = models.CharField(max_length=200)
    cognome = models.CharField(max_length=200)
    nazionalita = models.CharField(max_length=50)

    # __str__: definisce come la classe viene mostrata a display
    def __str__(self):
        return f'{self.nome} {self.cognome}, di nazionalità {self.nazionalita}'

class Lingua_og(models.Model):
    lingua_og = models.CharField(max_length=50)

    def __str__(self):
        return f'Lingua originale: {self.lingua_og}'
