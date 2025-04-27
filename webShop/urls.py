from django.urls import path # type: ignore
from webMyShop.views import index # type: ignore
from webShop import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'), 
]