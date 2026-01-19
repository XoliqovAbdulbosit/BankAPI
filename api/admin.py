from django.contrib import admin
from .models import Card, Transaction, Contact, Code

# Register your models here.
admin.site.register(Card)
admin.site.register(Transaction)
admin.site.register(Contact)
admin.site.register(Code)
