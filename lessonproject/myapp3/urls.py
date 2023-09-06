from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('hello2/', views.HelloView.as_view(), name='hello2'),
    # используем метод as_view() класса HelloView для создания объекта-обработчика запроса.
    path('posts/<int:year>/', views.year_post, name='year_post'),  # год статьи
    path('posts/<int:year>/<int:month>/', views.MonthPost.as_view(), name='month_post'),  # год и месяц статьи
    path('posts/<int:year>/<int:month>/<slug:slug>/', views.post_detail, name='post_detail'),
    # год, месяц и уникальный идентификатор статьи.
    path('', views.my_view, name='my_template'),
    # некий базовый адрес, который достаётся от адреса less3 из базового маршрутизатора
    path('if/', views.TemplIf.as_view(), name='templ_if'),
    path('for/', views.view_for, name='templ_for'),
    path('about/', views.about, name='about'),
    path('author/<int:author_id>/', views.author_posts, name='author_posts'),
    path('post/<int:post_id>/', views.post_full, name='post_full'),

]
"""
Преобразования пути - в параметры,
которые передаются обработчику
"""
