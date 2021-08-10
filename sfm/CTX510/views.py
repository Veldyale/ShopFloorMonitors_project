from django.shortcuts import render, get_object_or_404
from .models import *


def index(request):
    return render(request, 'CTX510/index.html')


def ctx510(request):
    return render(request, 'CTX510/ctx510.html')


def instr_ctx510(request):
    instructions = Instruction.objects.order_by('operation')
    return render(request, 'CTX510/instr_ctx510.html', {'title': 'Инструкции', 'instructions': instructions})


def manual_ctx510(request):
    manuals = Manual.objects.order_by('operation')
    return render(request, 'CTX510/manual_ctx510.html', {'title': 'Мануалы', 'manuals': manuals})


def circuit_ctx510(request):
    circuits = Circuit.objects.order_by('operation')
    return render(request, 'CTX510/circuit_ctx510.html', {'title': 'Схемы', 'circuits': circuits})


def catalog_ctx510(request):
    catalogs = Catalog.objects.order_by('operation')
    return render(request, 'CTX510/catalog_ctx510.html', {'title': 'Каталоги', 'catalogs': catalogs})
