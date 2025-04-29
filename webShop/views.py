from django.shortcuts import render # type: ignore
from .models import Produkt
from .forms import ProduktForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

# Create your views here.
def index(request):
    product = Produkt.objects.all()
    return render(request, 'produkty.html', {'product': product})

def admino(request):
    product = Produkt.objects.all()
    return render(request, 'admin.html', {'product': product})

def dodaj(request):
    if request.method == 'POST':
        form = ProduktForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Pomyślnie dodano")
            return redirect('admino')
    else:
        form = ProduktForm()
    return render(request, 'dodaj.html', {'form': form})

def edit_item(request, item_id):
    product = get_object_or_404(Produkt, id=item_id)
    if request.method == 'POST':
        form = ProduktForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Pomyślnie zaktualizowano")
            return redirect('admino')
    else:
        form = ProduktForm(instance=product)
    return render(request, 'edit-item.html', {'form': form, 'item': product})

def delete_item(request, item_id):
    product = get_object_or_404(Produkt, id=item_id)
    product.delete()
    messages.success(request, "Pomyślnie usunięto")
    return redirect('admino')

def delete_selected_items(request):
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_items')
        Produkt.objects.filter(id__in=selected_ids).delete()
        messages.success(request, "Pomyślnie usunięto zaznaczone elementy")
    return redirect('admino')