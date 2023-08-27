import requests
import .models
symbols="EUR,KZT,AED"
base="USD"
request=requests.get(f"http://api.exchangerate.host/latest?base={base}&symbols={symbols}", verify=False)

data=request.json()
base=data['base']
rates=data['rates']
date=data['date']

print(base, rates, date)