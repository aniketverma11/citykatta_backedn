from django.shortcuts import render

from .models import Transaction, Subscription
from rest_framework import viewsets

from .serializers import SubscriptionSerializer, TransactionSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
