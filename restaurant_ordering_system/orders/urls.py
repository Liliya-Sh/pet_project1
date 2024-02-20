from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'), #http://127.0.0.1:8000/
    # path('stages/', views.stages),  #http://127.0.0.1:8000/stages/
    path('cook/', views.cook, name='cook'),    #http://127.0.0.1:8000/cook/
    path('delivery/', views.deliveryman, name='delivery'),   #http://127.0.0.1:8000/delivery/
    path('orders_man/', views.orders_man, name='orders_man'),   #http://127.0.0.1:8000/orders_man/
]