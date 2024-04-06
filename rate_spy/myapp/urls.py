from django.urls import path
from .views import index_view, rating_view

urlpatterns = [
    path('index/', index_view, name='index_view'),
    path('rating/', rating_view, name='rating_view'),
]