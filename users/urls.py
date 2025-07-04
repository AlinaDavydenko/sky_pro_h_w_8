from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import PaymentViewSet

router = DefaultRouter()
router.register(r'payments', PaymentViewSet, basename='payments')

urlpatterns = [
    path('', include(router.urls)),
]
