'''
Módulo de URL de python
'''
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


# vista

def hello_world(resquest):
    '''

    :param resquest: Todas las vistas reciben si o si un request.
    :return: Es una respuesta, HTTP, se usa importando de django una herramienta. httpResponse.
    '''
    return HttpResponse('Hello-Daddy!')


urlpatterns = [
    # path('admin/', admin.site.urls),

    # '''
    # La función path() defino cual es la url que estoy esperando.
    # es decir su primer argumento es la rama que deriva la url, y el segundo argumento es lo que debe mostrar.
    # como la vista, en Django una vista es una función.
    # '''
    path('hello-world/', hello_world)

]
