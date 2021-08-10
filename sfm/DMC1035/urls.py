from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dmc1035/instructions', views.instr_dmc1035, name='instruction_dmc1035'),
    path('dmc1035/manuals', views.manual_dmc1035, name='manual_dmc1035'),
    path('dmc1035/circuits', views.circuit_dmc1035, name='circuit_dmc1035'),
    path('dmc1035/catalogs', views.catalog_dmc1035, name='catalog_dmc1035'),
    # path('<int:instruction_id>/', views.specific_instr_dmc1035, name='specific_instr_dmc1035')
]
