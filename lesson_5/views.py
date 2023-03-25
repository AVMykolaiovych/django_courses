from django.shortcuts import render
from django.http import HttpResponse
from .models import Flower, Bouquet, Client
from uuid import uuid4
from decimal import Decimal


from django.contrib.auth.models import User
from django.core.files import File


def create_flower(request):
    rose = Flower()
    rose.count = 5
    rose.description = "Rose is ..."
    rose.could_use_in_bouquet = True
    rose.wiki_page = "https://en.wikipedia.org/wiki/Rose"
    rose.name = "Rose"
    rose.save()
    return HttpResponse("Created!")


# def create_client(request):
#     with open('requirements.txt', 'r') as _file:
#         tmp_file = _file.read()
#
#     Client.objects.create(**{
#         'second_email': 'admin@admin1.com',
#         'name': 'MyName',
#         'invoice': tmp_file,
#         'user_uuid': uuid4(),
#         'discount_size': Decimal('0.00052'),
#         'client_ip': '192.0.2.1',
#     })
#     return HttpResponse("Created!")


def create_client(request):
    client = Client.objects.create(**{
        'user': User.objects.get(pk=1),
        'second_email': 'admin@admin1.com',
        'name': 'MyName',
        'invoice': File(open('requirements.txt')),
        'user_uuid': uuid4(),
        'discount_size': Decimal('0.00052'),
        'client_ip': '192.0.2.1',
    })
    print(client)
    return HttpResponse(client)


def get_flower(request):
    price = Bouquet.shop.get(id=1).price
    return HttpResponse(price)
