from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ctx310/instructions', views.instr_ctx310, name='instruction_ctx310'),
    path('ctx310/manuals', views.manual_ctx310, name='manual_ctx310'),
    path('ctx310/circuits', views.circuit_ctx310, name='circuit_ctx310'),
    path('ctx310/catalogs', views.catalog_ctx310, name='catalog_ctx310'),
    path('', include('CTX510.urls')),
    path('', include('DMC635.urls')),
    path('', include('DMC1035.urls')),
    path('', include('DMU50eco.urls')),
    path('', include('DMU50pre.urls')),

    # path('<int:instruction_id>/', views.specific_instr_ctx310, name='specific_instr_ctx310')
]
