from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PedidoConoViewSet

router = DefaultRouter()
router.register(r'pedidos_conos', PedidoConoViewSet, basename='pedidos_conos')

urlpatterns = [
    path('', include(router.urls)),
]