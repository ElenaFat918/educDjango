from django.shortcuts import render
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse("Hello, world!")


def about(request):
    try:
        # some code that might raise an exception
        result = 1 / 0
    except Exception as e:
        logger.exception(f'Error in about page: {e}')
        return HttpResponse("Oops, something went wrong.")
    else:
        logger.debug('About page accessed')
        return HttpResponse("This is the about page.")

"""
Функция index принимает объект request, который содержит информацию о запросе,
 и возвращает объект HttpResponse, который содержит ответ сервера. 
 В данном случае мы просто возвращаем текст "Hello, world!".  
 Вторая функция будет возвращать "About us". Пара простейших представлений созданы.
  Но работать они пока не будут. Необходимо настроить маршруты.
"""
