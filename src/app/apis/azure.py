from pprint import pprint
import json
import requests


URL= "https://prices.azure.com/api/retail/prices?api-version=2021-10-01-preview"
res= requests.get(url = URL)
data = res.json()
pprint(data)