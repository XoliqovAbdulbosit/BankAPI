from django.db import models


# Create your models here.
class Card(models.Model):
    number = models.CharField(max_length=16)
    phone_number = models.CharField(max_length=13)
    name = models.CharField(max_length=32)
    balance = models.IntegerField(default=0)
    photo = models.CharField(max_length=256)
    date = models.CharField(max_length=5, default="05/27")

    def __str__(self):
        return self.number


class Transaction(models.Model):
    sender = models.ForeignKey('Card', related_name='sender', on_delete=models.PROTECT)
    receiver = models.ForeignKey('Card', related_name='receiver', on_delete=models.PROTECT)
    amount = models.IntegerField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} {self.receiver}"


class Contact(models.Model):
    chat_id = models.IntegerField()
    phone_number = models.CharField(max_length=13)

    def __str__(self):
        return self.phone_number


class Code(models.Model):
    phone_number = models.CharField(max_length=13)
    code = models.CharField(max_length=6)

    def __str__(self):
        return self.phone_number
