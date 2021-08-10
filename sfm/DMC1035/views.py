from django.shortcuts import render, get_object_or_404
from .models import *


def index(request):
    return render(request, 'DMC1035/index.html')


def dmc1035(request):
    return render(request, 'DMC1035/dmc1035.html')


def instr_dmc1035(request):
    instructions = Instruction.objects.order_by('operation')
    return render(request, 'DMC1035/instr_dmc1035.html', {'title': 'Инструкции', 'instructions': instructions})


def manual_dmc1035(request):
    manuals = Manual.objects.order_by('operation')
    return render(request, 'DMC1035/manual_dmc1035.html', {'title': 'Мануалы', 'manuals': manuals})


def circuit_dmc1035(request):
    circuits = Circuit.objects.order_by('operation')
    return render(request, 'DMC1035/circuit_dmc1035.html', {'title': 'Схемы', 'circuits': circuits})


def catalog_dmc1035(request):
    catalogs = Catalog.objects.order_by('operation')
    return render(request, 'DMC1035/catalog_dmc1035.html', {'title': 'Каталоги', 'catalogs': catalogs})
