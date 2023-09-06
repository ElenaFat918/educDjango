from django.urls import path
from .views import total_in_db, total_in_view, total_in_template, main_myapp6

urlpatterns = [
    path('', main_myapp6, name='main_myapp6'),
    path('db/', total_in_db, name='db'),
    path('view/', total_in_view, name='view'),
    path('template/', total_in_template, name='template'),
]

