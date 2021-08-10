from django.shortcuts import render, get_object_or_404
from .models import *


def index(request):
    return render(request, 'CTX310/index.html')


def ctx310(request):
    return render(request, 'CTX310/ctx310.html')


def instr_ctx310(request):
    instructions = Instruction.objects.order_by('operation')
    return render(request, 'CTX310/instr_ctx310.html', {'title': 'Инструкции', 'instructions': instructions})


def manual_ctx310(request):
    manuals = Manual.objects.order_by('operation')
    return render(request, 'CTX310/manual_ctx310.html', {'title': 'Мануалы', 'manuals': manuals})


def circuit_ctx310(request):
    circuits = Circuit.objects.order_by('operation')
    return render(request, 'CTX310/circuit_ctx310.html', {'title': 'Схемы', 'circuits': circuits})


def catalog_ctx310(request):
    catalogs = Catalog.objects.order_by('operation')
    return render(request, 'CTX310/catalog_ctx310.html', {'title': 'Каталоги', 'catalogs': catalogs})
