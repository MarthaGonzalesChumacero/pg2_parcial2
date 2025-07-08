from rest_framework import serializers
from .models import PedidoCono
from .patrones import EstrategiaFactory


class PedidoConoSerializer(serializers.ModelSerializer):
    precio_final = serializers.SerializerMethodField()
    ingredientes_finales = serializers.SerializerMethodField()

    class Meta:
        model = PedidoCono
        fields = '__all__'  # Incluye cliente, variante, toppings, etc.
        read_only_fields = ['precio_final', 'ingredientes_finales']

    def get_precio_final(self, obj):
        estrategia = EstrategiaFactory.obtener_estrategia(obj.variante)
        return estrategia.calcular_precio(obj.tamanio_cono)

    def get_ingredientes_finales(self, obj):
        estrategia = EstrategiaFactory.obtener_estrategia(obj.variante)
        return estrategia.ingredientes_extra(obj.toppings)