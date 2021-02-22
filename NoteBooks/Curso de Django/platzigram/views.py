from django.http import HttpResponse
from datetime import  datetime
import  json



def hello_world(requests):
    '''

    :param requests:
    :return:

    1. Quiero traer la hora del servidor y convertirla  a un string que peuda verse.
    2. Puedo usar string format  para darle formato al tiempo. Con stringformattime
        %b : Mes
        %dth: Día
        %Y: Año
        %H: Horas
        %M: Minutos

    '''
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Son las {now}'.format(now =str(now)))


def another(request):
    '''

    :param arg:
    :return:

   Después de pasarla una serie de numeros como argumentos en la url, quiero que me los muestre en pantalla
   y que me los pase a un Json.


    '''
    numbers = request.GET['numbers'].split(',')
    numbers = sorted([int(i) for i in numbers])
    # import pdb;pdb.set_trace()
    data = {
        'status' :'ok',
        'numbers': numbers,
        'message': "Integers Sorted"
    }

    # Usamos el argumento contetn type
    return HttpResponse(json.dumps(data), content_type = "application/json")


def auth(request,name, age):
    '''

    :param request:
    :param name:
    :param age:
    :return:
    '''

    if age <12:
        m = 'No estas permitido {}'.format(name)
    else:
        m = 'Estas permitido {}'.format(name)
    return  HttpResponse(m)



