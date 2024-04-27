from rest_framework import serializers, permissions
from .models import Card, Transaction


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'number', 'phone_number', 'name', 'balance', 'photo']


class TransactionSerializer(serializers.ModelSerializer):
    sender = CardSerializer()
    receiver = CardSerializer()

    class Meta:
        model = Transaction
        fields = ['id', 'sender', 'receiver', 'amount']
