from ListePart.views import index,delete_data,update_data,liste
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('delete/<int:id>', delete_data, name='deletedata'),
    path('update/<int:id>/', update_data, name='updatedata'),
    path('liste', liste, name='liste'),
]
