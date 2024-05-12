from rest_framework import routers
from .views import SubscriptionViewSet, TransactionViewSet
from django.urls import include, path

router = routers.DefaultRouter()

router.register(r'subscriptions', SubscriptionViewSet)
router.register(r'transactions', TransactionViewSet)


urlpatterns = [
    path('payement/', include(router.urls)),
]
