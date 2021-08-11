from django.shortcuts import render, get_object_or_404
from .models import *


def kanban(request):
    return render(request, 'kanban/kanban.html')

def kanban(request):
    items = Item.objects.order_by('assembly_place')
    return render(request, 'kanban/kanban.html', {'id': 'id', 'items': items})
