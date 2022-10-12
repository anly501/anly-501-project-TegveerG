import requests
import json

# updated limit or num rows to most recent (10/10/2022) data

url = "https://api.s.defiyield.app/scam_database?sortField=fundsLost&sort=desc&sortDirection=desc&limit=3076&page=1"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

res_list = response.json()['items'] # items key is pertinent

with open('../../data/Raw Data/Python_REKT_Database_API/REKT_Database_Python_API.json', 'w') as json_file:
    json.dump(res_list, json_file) 
