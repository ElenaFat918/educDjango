from django.db import models
from datetime import datetime
from random import randint

"""
Создайте модель для запоминания бросков монеты: орёл или решка. 
Также запоминайте время броска.
"""

#
# class Kicks(models.Model):
#     result = models.BooleanField()
#     kick_time = models.DateTimeField(default=datetime.now())

"""
Доработаем задачу 
1. Добавьте статический метод для статистики по n последним броскам монеты. 
Метод должен возвращать словарь с парой ключей-значений, для орла и для решки.
"""


class Kicks(models.Model):
    result = models.BooleanField()
    kick_time = models.DateTimeField(default=datetime.now())

    @staticmethod
    def statistics(n: int):
        reshka = 0
        orel = 0
        for _ in range(n):
            kick = Kicks(result=randint(0, 1))
            if kick.result:
                reshka += 1
            else:
                orel += 1
            result_dict = {'орёл': orel, 'решка': reshka}
            return result_dict


"""
Создайте модель Автор. Модель должна содержать следующие поля:
● имя до 100 символов
● фамилия до 100 символов
● почта
● биография
● день рождения
Дополнительно создай пользовательское поле “полное имя”, которое возвращает имя и фамилию.
"""


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateTimeField()

    def __str__(self):
        return f'{self.name} {self.surname}'


# create_authors

"""
Создайте модель Статья (публикация). Авторы из прошлой задачи могут писать статьи.
У статьи может быть только один автор. У статьи должны быть следующие обязательные поля:
● заголовок статьи с максимальной длиной 200 символов
● содержание статьи
● дата публикации статьи
● автор статьи с удалением связанных объектов при удалении автора
● категория статьи с максимальной длиной 100 символов
● количество просмотров статьи со значением по умолчанию 0
● флаг, указывающий, опубликована ли статья со значением по умолчанию False
"""


class Article(models.Model):
    head = models.CharField(max_length=200)
    content = models.TextField()
    public_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    count = models.IntegerField(default=0)
    public = models.BooleanField()
