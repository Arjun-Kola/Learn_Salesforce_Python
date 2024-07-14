import pandas as pd
from simple_salesforce import Salesforce
from SalesForce_Basics.SF_Org_credentials import USERNAME, PASSWORD

CONSUMER_KEY = '3MVG9riCAn8HHkYXtQVtdXHODjNzdGR8wGts1BHkHUFhOf1cLSHHApOEAICJKlCdw0WCc80w4cIgcORk1iRTn'
CONSUMER_SECRET = 'C17A1E1BC6F727CB730836FE9E992AA81D2A0B1D3FDF552A2FF276C61ED7CBE0'


#Login to Salesforce org
sf = Salesforce(username=USERNAME, password=PASSWORD, consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)

Result_Dict = sf.query("Select id, name, Email from contact")
print(Result_Dict)
# PandasDataFrame = pd.DataFrame(Result_Dict)
# print(PandasDataFrame)

# res = sf.query_more("0038c000031ThWsAAK")
# print(res)

# List = sf.query_all("SELECT Id, Email FROM Contact")
# print(List)

# data = sf.query_all_iter("SELECT Id, Email FROM Contact WHERE LastName = 'Jones'")
# for row in data:
#     process(row)


