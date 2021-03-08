'''

Este archivo tiene como propósito probar la librería y poder de reuqest.
y conectar con token de github


'''

import requests as r

user = 'Alejandro-sin'
token ='14cdccc6e1f2e9bbbffcf65533c38ecdcc49db1e'

response = r.get('https://api.github.com/user', auth=(user, token))
print(response.content)