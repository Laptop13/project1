from django.contrib import admin

from .models import *

admin.site.register(Currency)
admin.site.register(ExchangeRate)
admin.site.register(UserExchangeRate)
admin.site.register(CurrencyPair)