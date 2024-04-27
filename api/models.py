from django.db import models


# Create your models here.
class Card(models.Model):
    number = models.CharField(max_length=16)
    phone = models.CharField(max_length=13)
    name = models.CharField(max_length=32)
    balance = models.IntegerField()
    photo = models.CharField(max_length=256)

    def __str__(self):
        return str(self.number)


class Transaction(models.Model):
    sender = models.ForeignKey('Card', related_name='sender', on_delete=models.PROTECT)
    receiver = models.ForeignKey('Card', related_name='receiver', on_delete=models.PROTECT)
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.sender} {self.receiver}"
