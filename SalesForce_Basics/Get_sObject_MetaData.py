import requests
from SalesForce_Basics.SF_Org_credentials import USERNAME, PASSWORD

CONSUMER_KEY = '3MVG9riCAn8HHkYXtQVtdXHODjNzdGR8wGts1BHkHUFhOf1cLSHHApOEAICJKlCdw0WCc80w4cIgcORk1iRTn'
CONSUMER_SECRET = 'C17A1E1BC6F727CB730836FE9E992AA81D2A0B1D3FDF552A2FF276C61ED7CBE0'
DOMAIN_NAME = 'https://creative-hawk-hhnodf-dev-ed.my.salesforce.com/'

json_data = {
    'grant_type': 'password',
    'client_id': CONSUMER_KEY,
    'client_secret': CONSUMER_SECRET,
    'username': USERNAME,
    'password': PASSWORD
}

response_access_token = requests.post(DOMAIN_NAME + '/services/oauth2/token', data=json_data)

print(response_access_token.status_code)
print(response_access_token.reason)
print(response_access_token.json())

if response_access_token.status_code == 200:
    access_token_id     = response_access_token.json()['access_token']

#Example to get a sObject metadata
headers = {
    'Authorization'  :  'Bearer ' + access_token_id
}

response_sObject    = requests.get(DOMAIN_NAME + '/services/data/v59.0/sobjects', headers = headers)
print(response_sObject.reason)
print(response_sObject.json())



