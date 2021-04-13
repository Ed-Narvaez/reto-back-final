"""Extras URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from compras import views

router = DefaultRouter()
router.register(r'compras/views/pasarela.html', views.CompraViewSet, basename='compras')

urlpatterns = [
    path('', include(router.urls))
]
