from django.shortcuts import render, get_object_or_404
from .models import *


def index(request):
    return render(request, 'DMu50eco/index.html')


def dmu50eco(request):
    return render(request, 'DMu50eco/dmu50eco.html')


def instr_dmu50eco(request):
    instructions = Instruction.objects.order_by('operation')
    return render(request, 'DMu50eco/instr_dmu50eco.html', {'title': 'Инструкции', 'instructions': instructions})


def manual_dmu50eco(request):
    manuals = Manual.objects.order_by('operation')
    return render(request, 'DMu50eco/manual_dmu50eco.html', {'title': 'Мануалы', 'manuals': manuals})


def circuit_dmu50eco(request):
    circuits = Circuit.objects.order_by('operation')
    return render(request, 'DMu50eco/circuit_dmu50eco.html', {'title': 'Схемы', 'circuits': circuits})


def catalog_dmu50eco(request):
    catalogs = Catalog.objects.order_by('operation')
    return render(request, 'DMu50eco/catalog_dmu50eco.html', {'title': 'Каталоги', 'catalogs': catalogs})
