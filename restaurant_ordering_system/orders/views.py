from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string

from orders.models import Order


# Create your views here.

def main_page(request):
    return HttpResponse("<h1>Наш супер-пупер модный сайт для ресторана!!!<h1>")

def stages(request):
    data = {'title': 'Этапы обработки заказа'}
    return render(request, 'orders/stages.html', data)

def cook(request):
    return HttpResponse("<h1>Заказы, которые надо приготовить</h1>")

def deliveryman(request):
    return HttpResponse("<h1>Заказы, которые надо доставить</h1>")

def orders_man(request):
    order = Order.objects.create(
        name='Егор',
        order='Рис с редиской',
        delivery=False,
        ready=True
    )
    return HttpResponse('Информация добавлена')
def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")