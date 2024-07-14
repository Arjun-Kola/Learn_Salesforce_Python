import pandas as pd
import requests
from SalesForce_Basics.SF_Org_credentials import USERNAME, PASSWORD

CONSUMER_KEY = '3MVG9riCAn8HHkYXtQVtdXHODjNzdGR8wGts1BHkHUFhOf1cLSHHApOEAICJKlCdw0WCc80w4cIgcORk1iRTn'
CONSUMER_SECRET = 'C17A1E1BC6F727CB730836FE9E992AA81D2A0B1D3FDF552A2FF276C61ED7CBE0'
DOMAIN_NAME = 'https://creative-hawk-hhnodf-dev-ed.my.salesforce.com/'


# Generate Access Token
def generate_token():
    PayLoad = {
        'grant_type': 'password',
        'client_id': CONSUMER_KEY,
        'client_secret': CONSUMER_SECRET,
        'username': USERNAME,
        'password': PASSWORD
    }

    token_response = requests.post(DOMAIN_NAME + '/services/oauth2/token', data=PayLoad)
    print(token_response.status_code)
    print(token_response.reason)
    # print(response_access_token.json())
    return token_response.json()


# Calling generate token function
access_token_id = generate_token()['access_token']

# Headers needs for request
headers = {
    'Authorization': 'Bearer ' + access_token_id
}


# Example 1:    Run a SOQL query
def query(soql_query):
    try:
        endpoint = 'services/data/v56.0/query/'
        records_list = []
        response = requests.get(DOMAIN_NAME + endpoint, headers=headers, params={'q': soql_query})
        total_size = response.json()['totalSize']
        print(response.json())
        records_list.extend(response.json()['records'])

        # while not response.json()['done']:
        #     print(response.json()['nextRecordsUrl'])
        #     response_urls = response.get(DOMAIN_NAME + endpoint + response.json()['nextRecordsUrl']),
        #     records_list.extend(response_urls.json()['records'])
        return {'record_size': total_size, 'records': records_list}
    except Exception as e:
        print(e)
        return

# Query#1
#         records_queried = query('SELECT id, name, type FROM opportunity')
#         print(records)
#         dataframe = pd.DataFrame(records_queried['records'])
#         print(dataframe)

records_queried  = query('Select id, name FROM Account')




# Example 2: Retrives an object's Metadata

def retrive_anObject_metaData(object_api_name):
    response_metadata = requests.get(DOMAIN_NAME + f'/services/data/v56.0/sobjects/{object_api_name}/describe', headers=headers)
    return response_metadata.json()

object_id = 'account'
object_metadata =  retrive_anObject_metaData(object_id)
#print(object_metadata)

df_metadata  = pd.DataFrame(object_metadata['fields'])
#print(df_metadata)

#df_metadata.to_csv('account metadata info.csv', index=False)




