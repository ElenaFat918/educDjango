﻿from django.urls import path
from .views import user_form, many_fields_form, upload_image, add_user

urlpatterns = [
    path('user/add/', user_form, name='user_form'),  # год и месяц статьи
    path('forms/', many_fields_form, name='many_fields_form'),
    path('user/', add_user, name='add_user'),
    path('upload/', upload_image, name='upload_image'),
]
"""
Преобразования пути - в параметры,
которые передаются обработчику
"""


