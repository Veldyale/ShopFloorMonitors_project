from django.shortcuts import render, get_object_or_404
from .models import *


def index(request):
    return render(request, 'DMu50pre/index.html')


def dmu50pre(request):
    return render(request, 'DMu50pre/dmu50pre.html')


def instr_dmu50pre(request):
    instructions = Instruction.objects.order_by('operation')
    return render(request, 'DMu50pre/instr_dmu50pre.html', {'title': 'Инструкции', 'instructions': instructions})


def manual_dmu50pre(request):
    manuals = Manual.objects.order_by('operation')
    return render(request, 'DMu50pre/manual_dmu50pre.html', {'title': 'Мануалы', 'manuals': manuals})


def circuit_dmu50pre(request):
    circuits = Circuit.objects.order_by('operation')
    return render(request, 'DMu50pre/circuit_dmu50pre.html', {'title': 'Схемы', 'circuits': circuits})


def catalog_dmu50pre(request):
    catalogs = Catalog.objects.order_by('operation')
    return render(request, 'DMu50pre/catalog_dmu50pre.html', {'title': 'Каталоги', 'catalogs': catalogs})
