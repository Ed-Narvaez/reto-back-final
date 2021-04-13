"""Extras URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from pedidos import views

router = DefaultRouter()
router.register(r'pedidos/views/resumen.html', views.PedidoViewSet, basename='pedidos')

urlpatterns = [
    path('', include(router.urls))
]
