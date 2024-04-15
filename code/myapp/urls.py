from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index_view, name='index_view'),
    path('', views.rating_view, name='rating_view'),
    path('table_result/', views.table_result_view, name='table_result_view'),
    path('graph_result/', views.graph_result_view, name='graph_result_view'),
]