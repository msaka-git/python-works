import requests

api_key = "bf9cdd15f4a19b5d87c30648f7493908"
url = "http://data.fixer.io/api/latest?access_key=" + api_key

first_currency = input("Birinci Para Birimi:").upper()  # Örnek : USD
second_currency = input("İkinci Para Birimi:").upper()  # Örnek : TRY
amount = int(input("Miktar:"))  # Örnek: 15

response = requests.get(url)

infos = response.json()

firstValue = infos["rates"][first_currency]
secondValue = infos["rates"][second_currency]

print((secondValue / firstValue) * amount)




