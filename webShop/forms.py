from django import forms # type: ignore

from .models import Produkt

class ProduktForm(forms.modelForm):
    class Meta:
        model = Produkt
        fields = ['nazwa', 'opis', 'cena', 'ilosc']