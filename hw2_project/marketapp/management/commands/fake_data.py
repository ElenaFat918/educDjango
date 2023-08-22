from django.core.management.base import BaseCommand
from marketapp.models import User, Product, Order


class Command(BaseCommand):
    help = "Generate fake clients, products and orders."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = User(name=f'Name{i}', email=f'mail{i}@mail.ru', telcontact=f'898765432{i}', adress=f'adress{i}')
            client.save()
            for j in range(1, count + 1):
                product = Product(name=f'NameProduct{j}',
                                  description=f'description from NameProduct{j} is bla bla bla many long text',
                                  price=f'{i}', quantity=f'{j}')
                product.save()
                for k in range(1, count + 1):
                    order = Order(customer=client, total_price=f'{i}')
                    order.save()
