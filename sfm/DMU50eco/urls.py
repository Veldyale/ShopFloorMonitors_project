from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dmu50eco/instructions', views.instr_dmu50eco, name='instruction_dmu50eco'),
    path('dmu50eco/manuals', views.manual_dmu50eco, name='manual_dmu50eco'),
    path('dmu50eco/circuits', views.circuit_dmu50eco, name='circuit_dmu50eco'),
    path('dmu50eco/catalogs', views.catalog_dmu50eco, name='catalog_dmu50eco'),
    # path('<int:instruction_id>/', views.specific_instr_dmu50eco, name='specific_instr_dmu50eco')
]
