from django.shortcuts import render
from .models import Products

def index(request):
    products = {
        "products": Products.objects.all(),
    }
    return render(request, "main/index.html",products)

def reports(request):
    return render(request, "main/reports.html")