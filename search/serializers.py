
# Django REST Framework
from rest_framework import serializers

# Models
from users.models import User
from experiences.models import Experience
from compras.models import Compra
from pedidos.models import Pedido
from carrito.models import Carrito


class ExperienceSerializer(serializers.ModelSerializer):
    """Experience Curriculum Model Serializer"""

    class Meta:
        """Meta class."""

        model = Experience
        fields = [
            'date_ini',
            'date_end',
            'company',
            'description',
        ]
class PedidoSerializer(serializers.ModelSerializer):
    """Experience Curriculum Model Serializer"""
    class Meta:
        """Meta class."""

        model = Pedido
        fields = [
            'title',
            'total',
            'descuento',
            'description',
        ]
class CompraSerializer(serializers.ModelSerializer):
    """Experience Curriculum Model Serializer"""

    class Meta:
        """Meta class."""

        model = Compra
        fields = [
            'title',
            'portada',
            'precio',
            'descuento',
            'description',
        ]
class CarritoSerializer(serializers.ModelSerializer):
    """Education Curriculum Model Serializer"""

    class Meta:
        """Meta class."""

        model = Carrito
        fields = [
            'date_ini',
            'total',
            'title',
        ]
