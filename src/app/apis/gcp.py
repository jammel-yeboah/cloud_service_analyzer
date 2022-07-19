from googleapiclient.discovery import build
from google.cloud import billing_v1
from pprint import pprint
import os
import json
import requests
import jellyfish
"""2nd thought
display form asking user for category, example: networking
then ask user to select category descriptions, example app moderization (gotten from google compare aws and azure services)
then get aws, azure and gcp services for given descirption(search map) AND send api request for each service
display 1st service region, sku_id and description for each service
calculate and display price for each service
diplay pricing difference of for aws, gcp, and azure"""


API_KEY= "AIzaSyBMgjO1cJZQVlqqyDoo2tOFsEHKmyCS9Wo"
API_SERVICE_NAME= "cloudbilling"
API_VERSION= 'v1'

# Add credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="auth/cp-calc-1-json-key.json"


#services
URL= f"https://cloudbilling.googleapis.com/v1/services?key={API_KEY}"
res= requests.get(url = URL)
data = res.json()

probability_match= 0
result= ""
for dict in data['services']:
    if (jellyfish.jaro_distance(dict['displayName'], "Firebase Auth")) > probability_match:
        probability_match= jellyfish.jaro_distance(dict['displayName'], "Firebase Auth")
        result= dict
print(result)


#sku
service_id= result['serviceId']
URL= f"https://cloudbilling.googleapis.com/v1/services/{service_id}/skus?key={API_KEY}"
r = requests.get(url = URL)
data = r.json()
pprint(data)

