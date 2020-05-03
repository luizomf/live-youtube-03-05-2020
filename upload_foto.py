import requests
from pprint import pprint
from get_token import token
from requests_toolbelt import MultipartEncoder
from mimetypes import MimeTypes

_print = print
print = pprint

mimetypes = MimeTypes()

nome_arquivo = 'python_logo.png'
mimetype_arquivo = mimetypes.guess_type(nome_arquivo)[0]

multipart = MultipartEncoder(fields={
    'aluno_id': '2',
    'foto': (nome_arquivo, open(nome_arquivo, 'rb'), mimetype_arquivo)
})


url = 'http://127.0.0.1:3001/fotos'

headers = {
    'Authorization': token,
    'Content-Type': multipart.content_type
}

response = requests.post(url=url, headers=headers, data=multipart)

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
