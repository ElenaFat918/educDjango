from django.urls import path
from .views import hello, HelloView
from .views import year_post, MonthPost, post_detail
from .views import my_view
from .views import HelloView, TemplIf




urlpatterns = [
    path('hello/', hello, name='hello'),
    path('hello2/', HelloView.as_view(), name='hello2'),    # используем метод as_view() класса HelloView для создания объекта-обработчика запроса.
    path('posts/<int:year>/', year_post, name='year_post'), # год статьи
    path('posts/<int:year>/<int:month>/', MonthPost.as_view(), name='month_post'),  # год и месяц статьи
    path('posts/<int:year>/<int:month>/<slug:slug>/', post_detail, name='post_detail'), #год, месяц и уникальный идентификатор статьи.
    path('', my_view, name='index'),    # некий базовый адрес, который достаётся от адреса less3 из базового маршрутизатора
    path('if/', TemplIf.as_view(), name='templ_if'),
]
"""
Преобразования пути - в параметры,
которые передаются обработчику
"""


