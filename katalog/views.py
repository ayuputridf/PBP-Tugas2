from django.shortcuts import render
from katalog.models import CatalogItem #Catalog Item lihat di class models.py


# TODO: Create your views here.
def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
    'list_barang': data_barang_katalog,
    'nama': 'Ayu Putri Dewi Fitriyani',
    'ID': '2106654845',
    }
    return render(request, "katalog.html", context)