"""Education URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from carrito import views

router = DefaultRouter()
router.register(r'carrito/views/carrito.html', views.CarritoViewSet, basename='carrito')

urlpatterns = [
    path('', include(router.urls))
]
