from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q


def kanban(request):
    search_query = request.GET.get('key_item', '')

    if search_query:
        items = Item.objects.filter(Q(baan_id__icontains=search_query) | Q(assembly_place__icontains=search_query) | Q(warehouse_place__icontains=search_query) | Q(size__icontains=search_query) | Q(iso__icontains=search_query) | Q(title__icontains=search_query))
    else:
        items = Item.objects.order_by('assembly_place')

    return render(request, 'kanban/kanban.html', {'id': 'id', 'items': items})
