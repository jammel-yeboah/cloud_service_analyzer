from pprint import pprint
import json
import requests
import jellyfish


def get_azure_info(product, region, category):
    data= find_product(product, region, category)
    if data== None: return None
    info= {'Name': data['productName'],
           'Usage Type': data['skuName'],
           'Service Regions': data['location'],
           'SKU ID': data['skuId'],
           'Price Description': f"{data['retailPrice']} USD per {data['unitOfMeasure']}"}
    return info




#recursively search pages until 50th page (skip 5,000) or category matches and prob match is higher than 0.8 and region matches
def find_product(product, region, category, skip=0, best_name_prob=0, best_match=None):
    URL= f"https://prices.azure.com/api/retail/prices?currencyCode='USD'&$filter=serviceFamily eq '{category}' and armRegionName eq '{region}' &$skip={skip}"
    res= requests.get(url = URL)
    data = res.json()
    if skip==5000: return best_match

    for i in range(len(data['Items'])):
        probability_match= jellyfish.jaro_distance(data['Items'][i]['serviceName'], product)#probabity for service name
        if  probability_match > best_name_prob:
            best_match= data['Items'][i]
            best_name_prob= probability_match
            if probability_match > 0.7: return data['Items'][i]
    return find_product(product, region, category, skip+100, best_name_prob, best_match)
