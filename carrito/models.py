from django.db import models
from users.models import User
from pedidos.models import Pedido

# django-ckeditor
from ckeditor.fields import RichTextField

class Carrito(models.Model):
    """Carrito model."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='autos')
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='marca')
    date_ini = models.DateTimeField()
    total = RichTextField(null=True)
    descuento = RichTextField(null=True)
