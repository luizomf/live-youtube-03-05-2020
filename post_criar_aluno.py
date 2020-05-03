import requests
from pprint import pprint
from get_token import token

_print = print
print = pprint

url = 'http://127.0.0.1:3001/alunos'

headers = {
    'Authorization': token
}

aluno_data = {
    "nome": "Luana 2",
    "sobrenome": "Vieira",
    "email": "luana2@email.com",
    "idade": "50",
    "peso": "80.04",
    "altura": "1.90"
}

response = requests.post(url=url, json=aluno_data, headers=headers)

if response.status_code >= 200 and response.status_code <= 299:
    # Sucesso
    print(response.status_code)
    print(response.reason)
    # print(response.text)

    response_data = response.json()
    print(response_data)
    # print('Bytes', response.content)
else:
    # Erros
    print(response.status_code)
    print(response.reason)
    print(response.text)
    # print('Bytes', response.content)
