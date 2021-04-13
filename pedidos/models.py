from django.db import models
from users.models import User

# django-ckeditor
from ckeditor.fields import RichTextField

class Pedido(models.Model):
    """Pedido model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pedido')
    title = models.CharField(max_length=255)
    total = RichTextField(null=True)
    description = RichTextField(null=True)
    descuento = RichTextField(null=True)
