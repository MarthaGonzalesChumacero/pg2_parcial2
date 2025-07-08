from rest_framework import serializers
from .models import PedidoCono, TOPPINGS_VALIDOS

class PedidoConoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoCono
        fields = ['cliente', 'variante', 'toppings', 'tamanio_cono']

    def validate_toppings(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Toppings debe ser una lista.")
        
        invalidos = [t for t in value if t not in TOPPINGS_VALIDOS]
        if invalidos:
            raise serializers.ValidationError(
                f"Los siguientes toppings no son válidos: {', '.join(invalidos)}"
            )
        
        return value