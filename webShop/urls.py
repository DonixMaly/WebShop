from django.urls import path # type: ignore
from webMyShop.views import index, admino # type: ignore
from webShop import admin, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'), 
    path('admino/', admino, name='admino')
]