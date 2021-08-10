from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dmu50pre/instructions', views.instr_dmu50pre, name='instruction_dmu50pre'),
    path('dmu50pre/manuals', views.manual_dmu50pre, name='manual_dmu50pre'),
    path('dmu50pre/circuits', views.circuit_dmu50pre, name='circuit_dmu50pre'),
    path('dmu50pre/catalogs', views.catalog_dmu50pre, name='catalog_dmu50pre'),
    # path('<int:instruction_id>/', views.specific_instr_dmu50pre, name='specific_instr_dmu50pre')
]
