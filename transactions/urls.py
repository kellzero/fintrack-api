from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet, register
from django.urls import path

router = DefaultRouter()
router.register(r'transactions', TransactionViewSet, basename='transaction')

urlpatterns = router.urls +[
    path('register/', register),
]