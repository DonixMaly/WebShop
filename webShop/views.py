from django.shortcuts import render # type: ignore
from .models import Produkt

# Create your views here.
def index(request):
    product = Produkt.objects.all()
    return render(request, 'produkty.html', {'product': product})