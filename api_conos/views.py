from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import PedidoCono
from .serializers import PedidoConoSerializer
from .factory import ConoFactory  # Corrige esto si tu archivo se llama factory.py (no factories)

class PedidoConoViewSet(viewsets.ModelViewSet):
    queryset = PedidoCono.objects.all()
    serializer_class = PedidoConoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            data = serializer.validated_data

            # Usamos tu lógica para generar el cono
            cono = ConoFactory.crear_cono(
                variante=data['variante'],
                tamanio=data['tamanio_cono']
            )

            # Creamos el pedido con todos los datos validados
            pedido = PedidoCono.objects.create(
                cliente=data['cliente'],
                variante=data['variante'],
                tamanio_cono=data['tamanio_cono'],
                toppings=data['toppings']
            )

            # Respondemos con los datos serializados del nuevo pedido
            response_serializer = self.get_serializer(pedido)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        # Si hay errores de validación, se devuelven aquí
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)