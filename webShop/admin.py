from django.contrib import admin # type: ignore
from .models import Produkt

# Register your models here.

@admin.register(Produkt)
class ProduktAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'cena', 'ilosc']
    search_fields = ['nazwa']