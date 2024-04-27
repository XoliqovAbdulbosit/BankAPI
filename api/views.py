import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from rest_framework import generics
from .models import Card, Transaction
from .serializers import CardSerializer, TransactionSerializer


# Create your views here.
class CardRead(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class TransactionRead(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


@csrf_exempt
@require_POST
def telegram_webhook(request):
    update = json.loads(request.body)
    if 'message' in update:
        chat_id = update['message']['chat']['id']
        print(chat_id, update['message'])

    return JsonResponse({'status': 'ok'})
