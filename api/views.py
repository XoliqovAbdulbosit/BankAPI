import json
from random import randint
import requests
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from rest_framework import generics
from .models import Card, Transaction, Contact, Code
from .serializers import CardSerializer, TransactionSerializer


# Create your views here.
class CardRead(generics.ListAPIView):
    serializer_class = CardSerializer

    def get_queryset(self):
        queryset = Card.objects.all()
        phone_number = self.request.query_params.get('phone_number', None)
        if phone_number:
            phone_number = f'+{phone_number.strip()}'
            queryset = queryset.filter(phone_number=phone_number)
        return queryset


class TransactionRead(generics.ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        queryset = Transaction.objects.all()
        phone_number = self.request.query_params.get('phone_number', None)
        card = self.request.query_params.get('card', None)
        if phone_number:
            phone_number = f'+{phone_number.strip()}'
            queryset = queryset.filter(Q(sender__phone_number=phone_number) | Q(receiver__phone_number=phone_number))
        if card:
            queryset = queryset.filter(Q(sender__number=card) | Q(receiver__number=card))
        return queryset


def send_message(chat_id, msg):
    token = '1463320976:AAFOq22eN4z4LlHrSLrxD2s39RmGUDNr5a8'
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text=Your verification code: {msg}'
    requests.get(url)


def check_phone_number(number):
    if number[0] == '+' and number[1:].isnumeric() and len(number[1:]) == 12:
        return True
    else:
        return False


@csrf_exempt
@require_POST
def telegram_webhook(request):
    update = json.loads(request.body)
    if 'message' in update:
        chat_id = update['message']['chat']['id']
        msg = update['message']['text']
        if check_phone_number(msg):
            Contact.objects.update_or_create(chat_id=chat_id, phone_number=msg)
            send_message(chat_id, 'Raqam qabul qilindi')
        else:
            send_message(chat_id, "Raqamni to'g'ri kiriting (+998901234567)")
    return JsonResponse({'status': 'Ok'})


@csrf_exempt
def send_code(request):
    phone_number = json.loads(request.body.decode('utf-8')).get('phone_number')
    if check_phone_number(phone_number):
        try:
            code = randint(100000, 999999)
            Code.objects.get_or_create(phone_number=phone_number, code=code)
            chat_id = Contact.objects.get(phone_number=phone_number).chat_id
            send_message(chat_id, code)
            return JsonResponse({'status': 'Verification code sent'})
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'Card or Verification Phone Number not found'})
    else:
        return JsonResponse({'status': 'Incorrect Phone Number'})


@csrf_exempt
def check_code(request):
    data = json.loads(request.body.decode('utf-8'))
    try:
        code = Code.objects.get(phone=data.get('phone_number'))
        if data.get('code') == code.code:
            code.delete()
            return JsonResponse({'status': 'Success'})
        else:
            return JsonResponse({'status': 'Fail'})
    except ObjectDoesNotExist:
        return JsonResponse({'status': 'Code not found'})


@csrf_exempt
def transaction(request):
    data = json.loads(request.body.decode('utf-8'))
    try:
        sender = Card.objects.get(number=data.get('sender'))
        receiver = Card.objects.get(number=data.get('receiver'))
        amount = data.get('amount')
        if sender.balance >= amount:
            sender.balance -= amount
            receiver.balance += amount
            Transaction.objects.create(sender=sender, receiver=receiver, amount=amount)
            sender.save()
            receiver.save()
            return JsonResponse({'status': 'Success'})
        else:
            return JsonResponse({'status': 'Sender Does Not Have Enough Funds'})
    except ObjectDoesNotExist:
        return JsonResponse({'status': 'Sender or Receiver Card not found'})
