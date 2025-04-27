from django.db import models

# Create your models here.

class Produkt(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.TextField()
    cena = models.FloatField(default=0)
    ilosc = models.IntegerField(default=0)

    def __str__(self):
        return self.name