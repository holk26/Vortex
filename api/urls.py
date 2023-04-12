from django.urls import path
from .views import TrasporteView, PedidoView, VehiculoView


urlpatterns = [
    path('conductor/', TrasporteView.as_view(), name='trasporte_list'),
    path('conductor/<int:id>', TrasporteView.as_view(), name='trasporte_process'),

    path('pedido/', PedidoView.as_view(), name='pedido_list'),
    path('pedido/<int:id>', PedidoView.as_view(), name='pedido_process'),

    path('vehiculos/', VehiculoView.as_view(), name='vehiculo_list'),
    path('vehiculos/<int:id>', VehiculoView.as_view(), name='vehiculo_process'),
]