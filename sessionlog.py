import requests 

# session using Session()
s = requests.Session()
s.headers.update({'Authorization': 'Bearer {token}'})
s.auth = ('accessid', 'password') #Set authorization for user access id and password


#Get link to go to 
r = s.get( "https://login.wayne.edu/")

#Check session status
print(f'Status Code: {r.status_code}, Content: {r.json()}')