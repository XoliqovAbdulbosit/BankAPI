from rest_framework import serializers
from .models import Card, Transaction


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'number', 'name', 'photo', 'balance', 'phone_number', 'date']


class TransactionSerializer(serializers.ModelSerializer):
    sender = CardSerializer()
    receiver = CardSerializer()
    datetime = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S")

    class Meta:
        model = Transaction
        fields = ['id', 'sender', 'receiver', 'amount', 'datetime']
