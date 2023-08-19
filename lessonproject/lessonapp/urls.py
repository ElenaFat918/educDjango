from django.urls import path
from . import views
"""cоединяем маршруты и представления"""
urlpatterns = [
    path('', views.index, name='index'),   # по пустому пути импортирую функцию index из модуля index и называю её index
    path('about/', views.about, name='about'),  # по пути about вызываю функцию about из модуля about и называю её about
]