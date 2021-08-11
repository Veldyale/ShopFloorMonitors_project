from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('dmc635/instructions', views.instr_dmc635, name='instruction_dmc635'),
    path('dmc635/manuals', views.manual_dmc635, name='manual_dmc635'),
    path('dmc635/circuits', views.circuit_dmc635, name='circuit_dmc635'),
    path('dmc635/catalogs', views.catalog_dmc635, name='catalog_dmc635'),
    # path('<int:instruction_id>/', views.specific_instr_dmc635, name='specific_instr_dmc635')
]
