from django.shortcuts import render

def index(request):
    return render(request, "main/index.html")

def reports(request):
    return render(request, "main/reports.html")