from django.urls import path
from . import views

urlpatterns = [
    path('stages/', views.stages),  #http://127.0.0.1:8000/orders/stages/
    path('cook/', views.cook),    #http://127.0.0.1:8000/orders/cook/
    path('delivery/', views.deliveryman),   #http://127.0.0.1:8000/orders/delivery/
]