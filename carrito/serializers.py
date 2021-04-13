
# Django REST Framework
from rest_framework import serializers
# Model
from carrito.models import Carrito

class CarritoModelSerializer(serializers.ModelSerializer):
    """Carrito Model Serializer"""

    class Meta:
        """Carrito class."""

        model = Carrito
        fields = (
            'pk',
            'pk',
            'date_ini',
            'total',
            'descuento',
        )

class CarritoSerializer(serializers.Serializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    pedido = serializers.HiddenField(default=serializers.CurrentUserDefault())
    date_ini = serializers.DateTimeField()
    total = serializers.CharField(max_length=10)
    descuento = serializers.CharField(max_length=2)

    def create(self, data):

        carrito = Carrito.objects.create(**data)
        return carrito
