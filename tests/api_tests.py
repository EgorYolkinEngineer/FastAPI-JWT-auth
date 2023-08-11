import pprint

import requests

response = requests.post('http://127.0.0.1:8000/auth/login/', json={
    'username': 'user',
    'password': '123'
})
result = response.json()
access_token = result['access_token']
# print(result)

# access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InVzZXIiLCJleHAiOjE2OTE3NzkzMDIsImlzX2FjY2VzcyI6dHJ1ZX0.jwBDNur9crxQmNavb5HpYGtVWo46IhtIv3PxzEMu-5s'

response = requests.get('http://127.0.0.1:8000/user/me/',
                        headers={
                            'Authorization': 'Bearer ' + access_token
                        })

result = response.json()

pprint.pprint(result)

#
# response = requests.post('http://127.0.0.1:8000/auth/register/', json={
#     'username': 'user',
#     'password': '123',
#     'name': 'Josh',
#     'surname': 'Vurgh',
#     'age': 18
# })
# print(response.json())
