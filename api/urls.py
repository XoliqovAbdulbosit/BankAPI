from django.urls import path
from .views import *

urlpatterns = [
    path('cards/', CardRead.as_view()),
    path('transactions/', TransactionRead.as_view()),
    path('telegram/webhook/', telegram_webhook),
    path('transaction/', transaction),
    path('send_code/', send_code),
    path('check_code/', check_code),
]
