from django.db import models


class Wallet(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    balance = models.IntegerField()

    class Meta:
        db_table = 'Wallets'

    def __str__(self):
        return self.name

    def earn(self, n):
        self.balance += n

    def spend(self, n):
        self.balance -= n