﻿*.\venv\Scripts\Activate.ps1*

*python manage.py startapp myapp3*

в settings добавьте приложение в константу со списком приложений

## Представления распологаются в файле views.py

Например, для функционального представления hello() и
классового представления HelloView можно определить URL-шаблоны
Создаём файл urls.py в каталоге приложения
Открываем urls.py в каталоге проекта и вносим в него изменения.

*python manage.py runserver*
http://127.0.0.1:8000/les3/hello
http://127.0.0.1:8000/les3/hello2

## Преобразование пути в типы Python

● str — приставка для передачи строки любых символов, кроме слэша.
Например, если мы хотим передать в представление информацию о
конкретном посте блога, то мы можем использовать такой путь:
path('posts/<str:slug>/', post_detail). Здесь slug - это строка символов, которая
является уникальным идентификатором поста.
● int — приставка для передачи целого числа. Например, если мы хотим
передать в представление информацию о конкретном пользователе по его
идентификатору, то мы можем использовать такой путь:
path('users/<int:id>/', user_detail). Здесь id - это целое число, которое является
уникальным идентификатором пользователя.
● slug — приставка для передачи строки, содержащей только буквы, цифры,
дефисы и знаки подчеркивания. Например, если мы хотим передать в
представление информацию о конкретной категории товаров, то мы можем
использовать такой путь:
path('categories/<slug:slug>/', category_detail). Здесь slug - это строка
символов, которая является уникальным идентификатором категории.
● uuid — приставка для передачи уникального идентификатора. Например, если
мы хотим передать в представление информацию о конкретном заказе, то мы
можем использовать такой путь:
path('orders/<uuid:pk>/', order_detail). Здесь pk - это уникальный
идентификатор заказа.
● path — приставка для передачи строки любых символов, включая слэши.
Например, если мы хотим передать в представление информацию о
конкретном файле на сервере, то мы можем использовать такой путь:
path('files/<path:url>/', file_detail). Здесь url - это строка символов, которая
содержит путь к файлу на сервере.

myapp3/urls.py

Снова возвращаемся к представлениям.
тестируем код, открываем браузер
http://127.0.0.1:8000/les3/posts/2022
http://127.0.0.1:8000/les3/posts/2022/6
http://127.0.0.1:8000/les3/posts/2022/6/python/

## Каталог шаблона

Внутри каталога приложения необходимо создать каталог templates. Далее в нём
создаётся каталог с именем приложения. Схема с двумя приложениями в проекте
ниже:
myproject/
myapp1/
templates/
myapp1/
index.html
...
...
myapp2/
templates/
myapp2/
index.html
...
...
myproject/
...
...
manage.py

вносим функцию во views и в urls приложения
проверяем
http://127.0.0.1:8000/les3/

## Проверка условия в шаблонах

создадим шаблон templ_if, вносим класс TemplIf в views и в urls приложения
проверяем
http://127.0.0.1:8000/les3/if

## Вывод в цикле

создадим шаблон templ_for.html, вносим класс TemplFor в views и в urls приложения
проверяем
http://127.0.0.1:8000/les3/for

## Наследование шаблонов Django

## Базовый шаблон проекта

Django позволяет создать базовый шаблон на уровне проекта.
settings.py:
Добавляем в список DIRS путь до каталога шаблона проекта BASE_DIR / 'templates'. 
Далее создаём каталог templates в каталоге BASE_DIR. Это каталог верхнего уровня. 
В нём находится файл manage.py, каталог проекта и каталоги приложений

myproject/ 
    myapp1/
    ... 
    myapp2/ 
    ... 
    myproject/ 
    ... 
    templates/ 
        base.html 
    ... 
    manage.py
Вкаталог помещаем базовый шаблон приложения base.html. 
Теперь команда расширения в дочерних шаблонах будет записываться без указания имени приложения:
{% extends 'base.html' %}

пропишем urls проекта путь к ''
from myapp3.views import index
path('', index),

# Объединяем модели,представления, шаблоны и маршруты
Создание моделей
возьмем из урока 2
*python manage.py makemigrations myapp3*
*python manage.py migrate*

Наполнение фейковыми данными
создадим файл myapp3/management/commands/ﬁll_db.py
Для заполнения базы семью авторами необходимо выполнить команду 
python manage.py fill_db 7
## Представления
Представление автора 
Создадим“вьюшку”для получения 5 последних статей автора

Маршруты
Сразу пропишем маршруты для вновь созданных представлений в файле urls.py

Шаблоны
Базовый шаблон 
Начнём с простейшего базового шаблона. 
При желании добавить шапку и подвал в будущем,
правки нужно делать только в нём. Создадим base.html
```commandline
<!--<!DOCTYPE html>-->
<!--<html lang="ru">-->
<!--    <head>-->
<!--        <meta charset="UTF-8">-->
<!--        <title>{% block title %}Сайт{% endblock %}</title>-->
<!--</head>-->
<!--<body>-->
<!--    {% block content %}-->
<!--        <p>Скоро тут появится текст...</p>-->
<!--    {% endblock %}-->
<!--    <footer>Базовый шаблон проекта</footer>>-->
<!--</body>-->
<!--</html>-->


<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Блог{% endblock %}</title>
</head>
<body>
    {% block content %}
    <p>Контент скоро появится ...</p>
    {% endblock %}
</body>
</html>

```

Внимание! Расположите базовый шаблон в каталоге templates проекта. Дочерние шаблоны сохраняйте в каталоге 
templates/myapp3/ приложения.

author_posts.html 
```
{% extends 'base.html' %}

{% block title %}{{ author.name }}'s Posts{% endblock %}

{% block content %}
    <h2>Последние 5 статей автора: {{ author.name }}</h2>
    <table>
        {% for post in posts %}
            <tr>
                <td><a href="{% url 'post_full' post.id %}">{{ post.title }}</a>
                <td>{{ post.get_summary }}</td>
            </tr>
        {% endfor %}
    </table>
{% endblock %}
<!--&lt;!&ndash;Внутри шаблона мы обращаемся к переменным author и post как к экземплярам класса. -->
<!--Для получения имени автора используем точечную нотацию author.name, -->
<!--т.к. это свойство прописано в моделе автора. Аналогично получаем заголовок статьи. -->
<!--Кроме того в моделе Post есть метод get_summary. Он возвращает 12 первых слов из содержимого статьи. -->
<!--Используя {{ post.get_summary }} шаблон через контекст вызываетметодмодели.-->
<!-- Отдельноговниманиязаслуживаеттегurl.Посленеговкавычкахмыуказываемимя представления, -->
<!-- которое хотим вызвать. Внимательно посмотрите на строку из urls.py path('post/<int:post_id>/', post_full, name='post_full'),&ndash;&gt;-->
<!--Мы можем обращаться к post_full по имени, потому что прописали ключевой аргументnameвфункцииpath.-->
<!--Передача значения post.id позволяет задать значение параметра post_id внутри представленияpost_full.-->
```
```commandline
{% extends 'base.html' %}

{% block title %}{{ post.title }}{% endblock %}

{% block content %}
    <h3>{{ post.title }}</h3>
    <p>{{ post.content }}</p>
{% endblock %}

В шаблоне мы также переопределили блок title и добавили содержимое в блок content.
Выводим заголовок и полный текст поста 
```