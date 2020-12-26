'''

Voy a mandar datos con PUT, PATCH, POST


Debo saber conectar con APIS

API ejemplo: https://jsonplaceholder.typicode.com/posts
'''

import requests as rq
import json

api_url = 'https://jsonplaceholder.typicode.com/posts'

# GET
response = rq.get(api_url)
# Me retorna algo de clase bytes.
content = response.content
data = json.loads(content)
print(data[0:1])


# POST


input_data = {'user_Id':5,
              'title': "Annymadversion",}
post = rq.post(api_url, input_data)
data_posted = json.loads(post.content)

'''
Cabe aclarar que el id se puso solo como 101, pero dónde está viviendo esta URL? Ciertamente
no es dentro de lo que es la api como tal, porque está intacta, pero si cuenta con los 100 elemntos virtualemnte
y me cuenta en 101.
'''
print(data_posted)

'''
Investigar patch  y put para que me sirven

'''


'''
Si quiero modificar lso encabezados

'''

input_data = json.dumps({'title':'Sit cibo, sit es '})
headers = {'Content-Type':'Application/json'}
r = rq.post(api_url, input_data,headers=headers)
data = json.loads(r.content)
print(data)
