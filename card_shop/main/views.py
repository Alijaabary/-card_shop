from django.shortcuts import render
from django.http import HttpResponse

def main_view(request):
    return render(request, "main.html", {"name": "CardShop"})
# Create your views here.
