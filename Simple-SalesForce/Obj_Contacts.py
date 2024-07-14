from simple_salesforce import Salesforce
from SalesForce_Basics.SF_Org_credentials import USERNAME, PASSWORD

CONSUMER_KEY = '3MVG9riCAn8HHkYXtQVtdXHODjNzdGR8wGts1BHkHUFhOf1cLSHHApOEAICJKlCdw0WCc80w4cIgcORk1iRTn'
CONSUMER_SECRET = 'C17A1E1BC6F727CB730836FE9E992AA81D2A0B1D3FDF552A2FF276C61ED7CBE0'


#Login to Salesforce org
sf = Salesforce(username=USERNAME, password=PASSWORD, consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)

##Create a contact record
contactDict = sf.Contact.create({'LastName':'Smith','Email':'example@example.com'})
print(contactDict)

##Get a contact record
contact = sf.Contact.get('0038c00003QvJsKAAV')
#print(contact)







