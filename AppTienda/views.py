from django.shortcuts import render
from .models import Combo

# Create your views here.
def home(request):
    combosListado= Combo.objects.all()
    return render(request,"gestion.html", {"combos":combosListado})