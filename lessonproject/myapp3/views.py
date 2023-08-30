from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render # функция render упрощает объем кода
from django.views.generic import TemplateView

# Функциональное представление 
def hello(request):
    return HttpResponse('Hello world from function!')


# Классовое представление
class HelloView(View):  # определяем класс, который наследуется от базового
# класса View из модуля django.views и реализует один или несколько методов для обработки запросов
    def get(self, request):
        return HttpResponse("Hello World from class!")


def year_post(request, year):
    text = ""
    ... # формируем статьи за год
    return HttpResponse(f"Posts from {year}<br>{text}")

# Это представление будет доступно по адресу http://127.0.0.1:8000/les3/posts/2022/
# При этом год может быть любым целым числом.

#### Представление через класс возвращает HttpResponse

class MonthPost(View):
    def get(self, request, year, month):
        text = ""
        ... # формируем статьи за год и месяц
        return HttpResponse(f"Posts from {month}/{year}<br>{text}")

# можно перейти по адресу http://127.0.0.1:8000/les3/posts/2022/6/

# Представление через функцию возвращает JSON

def post_detail(request, year, month, slug):
    ... # Формируем статьи за год и месяц по идентификатору.
    # Пока обойдёмся без запросов к базе данных
    post = {
        "year": year,
        "month": month,
        "slug": slug,
        "title": "Кто быстрее создаёт списки в Python, list() или []",
        "content": "В процессе написания очередной программы задумался над тем,\
        какой способ создания списков в Python работает быстрее...",
    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii':False})


"""    
В отличии от двух первых представлений, третье возвращает JSON объект.
Очевидное изменение — использование JsonResponse вместо привычного
HttpResponse. Менее очевидное - русский текст. А если быть более точным, текст в
кодировке UTF-8, а не в ASCII(кодировка аскей - только латинский алфавит). Для этого мы передаём дополнительный параметр
json_dumps_params={'ensure_ascii': False}   -параметры для преобр json-объекта . Если вы работали с модулем json из
стандартной библиотеки Python, параметр ensure_ascii вам знаком. Он
подтверждает, что JSON будет содержать не только 127 символов из кодировки
ASCII.
Проверить работу представления можно по адресу наподобие
http://127.0.0.1:8000/les3/posts/2022/6/python/
"""

def my_view(request):
        context = {"name": "John"}
        return render(request, "myapp3/my_template.html", context)  # render принимает на вход три аргумента: объект запроса от пользователя, шаблон кот будем использовать, словарь со значением name и ответом John

# пропишем url в приложении

class TemplIf(TemplateView):    # наследуется от TemplateView и указывает на использование шаблона myapp3/templ_if.html.
    template_name = "myapp3/templ_if.html"  # template_name - зарезервированное имя, его будет искать джанго для поиска шаблона если используется представление на основе класса
    
    def get_context_data(self, **kwargs):   # **kwargs - распаковка словаря
        context = super().get_context_data(**kwargs)  #добавляем две переменные в словарь context - message и number, помимо контекста из **kwargs мы используем свой context и егог возвращаем
        context['message'] = "Привет, мир!"
        context['number'] = 5
        return context

# пропишем url в приложении

#  представлениt на основе функции с передачей списка и словаря в контексте

def view_for(request):
    my_list = ['apple', 'banana', 'orange']
    my_dict = {
        'каждый': 'красный',
        'охотник': 'оранжевый',
        'желает': 'жёлтый',
        'знать': 'зелёный',
        'где': 'голубой',
        'сидит': 'синий',
        'фазан': 'фиолетовый',
    }
    context = {'my_list': my_list, 'my_dict': my_dict}
    return render(request, 'myapp3/templ_for.html', context)