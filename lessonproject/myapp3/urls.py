from django.urls import path
from .views import hello, HelloView
from .views import year_post, MonthPost, post_detail
from .views import my_view
from .views import HelloView
from .views import TemplIf
from .views import view_for
from .views import index, about
from .views import author_posts, post_full


urlpatterns = [
    path('hello/', hello, name='hello'),
    path('hello2/', HelloView.as_view(), name='hello2'),
    # используем метод as_view() класса HelloView для создания объекта-обработчика запроса.
    path('posts/<int:year>/', year_post, name='year_post'),  # год статьи
    path('posts/<int:year>/<int:month>/', MonthPost.as_view(), name='month_post'),  # год и месяц статьи
    path('posts/<int:year>/<int:month>/<slug:slug>/', post_detail, name='post_detail'),
    # год, месяц и уникальный идентификатор статьи.
    path('', my_view, name='index'),
    # некий базовый адрес, который достаётся от адреса less3 из базового маршрутизатора
    path('if/', TemplIf.as_view(), name='templ_if'),
    path('for/', view_for, name='templ_for'),
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('author/<int:author_id>/', author_posts, name='author_posts'),
    path('post/<int:post_id>/', post_full, name='post_full'),

]
"""
Преобразования пути - в параметры,
которые передаются обработчику

Мы создаем два URL-адреса - для представлений author_posts и post_full. 
В обоих случаях мы используем целочисленный параметр в URL для передачи id автора и поста соответственно. 
Мы также добавляем имена для каждого URL-адреса, чтобы мы могли ссылаться на них в шаблонах с помощью 
тега url. 
"""
