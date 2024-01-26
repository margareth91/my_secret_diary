from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('entry_list/', views.entry_list, name='entry_list'),
    path('entry/<int:entry_id>/', views.entry_detail, name='entry_detail'),
    path('entry/new_entry/', views.new_entry, name='new_entry'),
]
