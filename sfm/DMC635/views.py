from django.shortcuts import render, get_object_or_404
from .models import *


def index(request):
    return render(request, 'DMC635/index.html')


def dmc635(request):
    return render(request, 'DMC635/dmc635.html')


def instr_dmc635(request):
    instructions = Instruction.objects.order_by('operation')
    return render(request, 'DMC635/instr_dmc635.html', {'title': 'Инструкции', 'instructions': instructions})


def manual_dmc635(request):
    manuals = Manual.objects.order_by('operation')
    return render(request, 'DMC635/manual_dmc635.html', {'title': 'Мануалы', 'manuals': manuals})


def circuit_dmc635(request):
    circuits = Circuit.objects.order_by('operation')
    return render(request, 'DMC635/circuit_dmc635.html', {'title': 'Схемы', 'circuits': circuits})


def catalog_dmc635(request):
    catalogs = Catalog.objects.order_by('operation')
    return render(request, 'DMC635/catalog_dmc635.html', {'title': 'Каталоги', 'catalogs': catalogs})
