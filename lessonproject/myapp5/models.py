from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # blank - указали обязательное ли для заполнения поле, необяз -True
    description = models.TextField(default='', blank=True)
    # DecimalField - для точности, 2 цифры после запятой
    price = models.DecimalField(default=999999.99, max_digits=8, decimal_places=2)
    # PositiveSmallIntegerField - положительное 2байта для хранения 0-32000
    quantity = models.PositiveSmallIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    # rating - рейтинг продуктов от 0,0 до 9,99
    rating = models.DecimalField(default=5.0, max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name
