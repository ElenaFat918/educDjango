
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('coin/', views.coin, name='coin'),
    path('cube/', views.cube, name='cube'),
    path('rand100/', views.rand100, name='rand100'),
    path('about/', views.about, name='about'),
]