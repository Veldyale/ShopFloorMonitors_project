from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('ctx510/instructions', views.instr_ctx510, name='instruction_ctx510'),
    path('ctx510/manuals', views.manual_ctx510, name='manual_ctx510'),
    path('ctx510/circuits', views.circuit_ctx510, name='circuit_ctx510'),
    path('ctx510/catalogs', views.catalog_ctx510, name='catalog_ctx510'),
    # path('<int:instruction_id>/', views.specific_instr_ctx510, name='specific_instr_ctx510')
]
