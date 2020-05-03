import requests
from pprint import pprint
_print = print
print = pprint

url = 'http://127.0.0.1:3001/tokens'

user_data = {
    "password": "123456",
    "email": "luiz@email.com"
}

response = requests.post(url=url, json=user_data)

if response.status_code >= 200 and response.status_code <= 299:
    # Sucesso
    print(response.status_code)
    print(response.reason)
    # print(response.text)

    response_data = response.json()
    token = response_data['token']

    with open('token.txt', 'w') as file:
        file.write(token)

    # print('Bytes', response.content)
else:
    # Erros
    print(response.status_code)
    print(response.reason)
    print(response.text)
    # print('Bytes', response.content)
