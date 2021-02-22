

'''

Extraigo las preguntas en for de texto, ahora, como le quito los dos
patrones que trae?

<p><strong>
</strong> </p>

todos = soup.find_all('p')
print(type(todos))

# <class 'bs4.element.ResultSet'>

uno = soup.find('p')
print(type(uno))

# <class 'bs4.element.Tag'>

print(todos)


'''


import requests as rq
from bs4 import BeautifulSoup as bs

URL= "https://www.guru99.com/javascript-interview-questions-answers.html"
response = rq.get(URL).content
soup = bs(response, 'lxml')

# PREGUNTAS: Trae todos los valores de p converitdos es una lista sin etiquetas.
namelist = soup.find_all('p')
questions =[]
for name in namelist:
    name = str(name)
    if name.startswith("<p><strong>"):
        name = name.replace('<p><strong>',"")
        name = name.replace('</strong> </p>', "")
        questions.append(name)

for a in  questions:
    print(a)


# RESPUESTAS: Trae todos los valores de p que son respuestas.

#
# answers =[]
# for answer in namelist:
#     answer = str(answer)
#     if not answer.startswith("<p><strong>"):
#         answer = answer.replace('<p><strong>', "")
#         answer = answer.replace('</strong> </p>', "")
#         answers.append(answer)
# # print(answer)




