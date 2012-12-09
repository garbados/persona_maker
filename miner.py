import requests
import json
from settings import url, api_key, email_list

with open(email_list, 'r') as f:
    emails = eval(f.read())

user_data = []

for email in emails:
    params = dict(email=email, apiKey=api_key)
    r = requests.get(url, params=params)
    if r.status_code == 403:
        print "Quota exceeded!"
        break
    profile = json.loads(r.text)
    user_data.append(profile)
    try:
        print "Grabbed %s" % profile['contactInfo']['fullName']
    except KeyError:
        print "Grabbed a dude with no name"

with open('data/user_data', 'w') as f:
    f.write(str(user_data))