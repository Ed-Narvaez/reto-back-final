
# Django REST Framework
from rest_framework import serializers
# Model
from pedidos.models import Pedido

class PedidoModelSerializer(serializers.ModelSerializer):
    """Extras Model Serializer"""

    class Meta:
        """Meta class."""

        model = Pedido
        fields = (
            'pk',
            'title',
            'total',
            'descuento',
            'description',
        )

class PedidoSerializer(serializers.Serializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=5000)
    descuento = serializers.CharField(max_length=2)
    total = serializers.CharField(max_length=10)
    
    def create(self, data):

        pedido = Pedido.objects.create(**data)
        return pedido
