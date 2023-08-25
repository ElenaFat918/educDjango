from django.shortcuts import render
from django.http import HttpResponse
from random import randint
import logging

logger = logging.getLogger(__name__)


def text(title, result):
    return f'<h1>{title}</h1>' \
           f'<p>Результат для вас: {result}</p>'

def index(request):
    title = 'index'
    return HttpResponse("Добавьте в путь: /coin или /cube или /rand100 ")


def coin(request):
    title = 'Бросок монеты'
    temp = randint(1, 2)
    if temp == 1:
        result = 'Решко'
    else:
        result = 'Орел'
    logger.info(f'Сгенерировано значение - {result}')
    return HttpResponse(text(title, result))


def cube(request):
    title = 'Бросок кубика'
    result = randint(1, 6)
    logger.info(f'Сгенерировано значение - {str(result)}')
    return HttpResponse(text(title, result))


def rand100(request):
    title = 'Значение из 100'
    result = randint(0, 100)
    logger.info(f'Сгенерировано значение - {str(result)}')
    return HttpResponse(text(title, result))