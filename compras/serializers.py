
# Django REST Framework
from rest_framework import serializers
# Model
from compras.models import Compra

class CompraModelSerializer(serializers.ModelSerializer):
    """Marcas Model Serializer"""

    class Meta:
        """Meta class."""

        model = Compra
        fields = (
            'pk',
            'title',
            'portada',
            'precio',
            'descuento',
            'description',
        )

class CompraSerializer(serializers.Serializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    title = serializers.CharField(max_length=255)
    precio = serializers.CharField(max_length=10)
    descuento = serializers.CharField(max_length=2)
    portada = serializers.FileField(default=serializers.CurrentUserDefault())
    description = serializers.CharField(max_length=5000)

    def create(self, data):

        compra = Compra.objects.create(**data)
        return compra
