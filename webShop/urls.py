from django.urls import path # type: ignore
from webMyShop.views import index, admino, dodaj, edytuj, usun, usun_produkt # type: ignore
from webShop import admin, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('admino/', admino, name='admino'),
    path('admino/dodaj', dodaj, name='dodaj'),
    path('admino/edytuj/<int:produkt_id>/', edytuj, name='edytuj'),
    path('admino/usun/<int:produkt_id>', usun, name='usun'),
    path('admino/usun_produkt', usun_produkt, name='usun_produkt'),
]