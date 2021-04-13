from django.db import models
from users.models import User

# django-ckeditor
from ckeditor.fields import RichTextField
from ckeditor.fields import FileField

class Compra(models.Model):
    """Marca model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Marca')
    title = models.CharField(max_length=255)
    portada = FileField(null=True)
    precio = RichTextField(null=True)
    descuento = RichTextField(null=True)
    description = RichTextField(null=True)
