import logging

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .forms import UserForm, ManyFieldsForm
from .forms import ImageForm
from .models import User

logger = logging.getLogger(__name__)


def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            # Делаем что-то с данными
            logger.info(f'Получили {name=}, {email=}, {age=}.')
    else:
        form = UserForm()
    return render(
        request,
        'myapp4/user_form.html',
        {'form': form})


"""В данном случае мы импортируем модуль render для рендеринга шаблона, а также
импортируем нашу форму UserForm. Далее определяем функцию user_form, которая
будет обрабатывать запросы на адрес /user_form/.
Если запрос пришел методом POST, то мы создаем экземпляр формы UserForm с
переданными данными из запроса. Если форма проходит валидацию (все поля
заполнены корректно), то мы получаем данные из формы и можем с ними работать.
Если запрос пришел методом GET, то мы просто создаем пустой экземпляр формы
UserForm и передаем его в шаблон user_form.html."""


def many_fields_form(request):
    if request.method == 'POST':
        form = ManyFieldsForm(request.POST)
        if form.is_valid():
            # Делаем что-то с данными
            logger.info(f'Получили {form.cleaned_data=}.')
    else:
        m = ManyFieldsForm()
    return render(request, 'myapp4/many_fields_form.html', {'form': form})

    """
    Стандартный вывод пустой формы при GET запросе и формирование формы с данными при POST запросе с последующей 
    проверкой и возможной обработкой.
"""


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            logger.info(f'Получили {name=}, {email=}, {age=}.')
            user = User(name=name, email=email, age=age)
            user.save()
            message = 'Пользователь сохранён'
    else:
        form = UserForm()
        message = 'Заполните форму'
        return render(request, 'myapp4/user_form.html', {'form': form, 'message': message})


"""
Если форма отправлена как POST запрос и проверки данных прошли успешно,
получаем переданные данные и создаём экземпляр класса User. Метод user.save()
сохраняет запись в таблицу БД
"""


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
        return render(request, 'myapp4/upload_image.html', {'form': form})
