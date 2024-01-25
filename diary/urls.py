from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('entry_list/', views.entry_list, name='entry_list')
]
