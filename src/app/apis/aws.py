import boto3
from pprint import pprint
import json

client = boto3.client('pricing',
                      aws_access_key_id="AKIA3I2QDT7JF5RTK5VJ",
                      aws_secret_access_key="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",
                      region_name= 'us-east-1')

services = client.describe_services(
    FormatVersion='aws_v1',
    MaxResults=100
)

product= client.get_products(
    ServiceCode='AmazonChimeFeatures',
    MaxResults=100
)



###add select region