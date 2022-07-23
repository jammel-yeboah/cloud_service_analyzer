import boto3
from pprint import pprint
import json
import ast
import jellyfish
import os
from decouple import config



client = boto3.client('pricing',
                      aws_access_key_id=config('AWS_ACCESS_KEY', default='None'),
                      aws_secret_access_key=config('AWS_SECRET_ACCESS_KEY', default='None'),
                      region_name= 'us-east-1')

def get_aws_info(product, region=None):
    #get list of services
    services = client.describe_services(FormatVersion='aws_v1')
    #find available service that closely mathces input
    probability_match= 0
    productMatch= None
    for i in range(len(services['Services'])):
        if (jellyfish.jaro_distance(services['Services'][i]['ServiceCode'], product)) > probability_match:
            probability_match= jellyfish.jaro_distance(services['Services'][i]['ServiceCode'], product)
            productMatch= services['Services'][i]['ServiceCode']


    #get list of product and info for service
    products= client.get_products(ServiceCode=productMatch)
    #find product in given region
    d= None #to be used as dictionary object
    for i in range(len(products['PriceList'])):
        d= (products['PriceList'][i])
        d= ast.literal_eval(d)
        if region in d['product']['attributes']['location']:
            break

    #parse/get data from dict d
    displayName= d['product']['attributes']['servicename']
    usageType= d['product']['attributes']['usagetype']
    serviceRegions= d['product']['attributes']['location']
    skuId= d['product']['sku']

    key1= list(d['terms']['OnDemand'].keys())[0]    #some keys are not consistent accross all products
    key2= list(d['terms']['OnDemand'][key1]['priceDimensions'].keys())[0]   #key1 and key2 gets them
    priceDescription= d['terms']['OnDemand'][key1]['priceDimensions'][key2]['description']  #apply keys

    info= {'Name': displayName,'Usage Type': usageType, 'Service Regions': serviceRegions, 'SKU ID': skuId, 'Price Description': priceDescription}
    return info
