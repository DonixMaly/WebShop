from django.urls import path
from webMyShop.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'), 
]