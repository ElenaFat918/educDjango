from datetime import date
from random import choice, randint, uniform
from django.core.management.base import BaseCommand
from hw_app.models import Product


class Command(BaseCommand):
    help = "Generate fake products."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        products = []
        count = kwargs.get('count')
        for i in range(1, count + 1):
            products.append(Product(name=f'продукт номер {i}',
                                    content='спортивный автомобиль. Производство "".',
                                    price=uniform(0.01, 999_999.99), count=randint(1, 10_000),
                                    add_day=date.today(),
                                    image=None
                                    ))
        Product.objects.bulk_create(products)
