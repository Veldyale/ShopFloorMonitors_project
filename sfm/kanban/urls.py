from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('kanban', views.kanban, name='kanban'),
    # path('<int:instruction_id>/', views.specific_instr_dmu50pre, name='specific_instr_dmu50pre')
]
