from django.contrib.auth.models import User
from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.code

class CurrencyPair(models.Model):
    from_currency = models.ForeignKey(Currency, related_name='exchange_rates', on_delete=models.CASCADE)
    to_currency = models.ForeignKey(Currency, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.from_currency)+"/"+str(self.to_currency)

class ExchangeRate(models.Model):
    rate = models.DecimalField(max_digits=10, decimal_places=4)
    date = models.DateField()
    currency_pair = models.ForeignKey(CurrencyPair, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.currency_pair.from_currency} to {self.currency_pair.to_currency}: {self.rate}"

class UserExchangeRate(models.Model):
    exchange_rate = models.ForeignKey(ExchangeRate, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
