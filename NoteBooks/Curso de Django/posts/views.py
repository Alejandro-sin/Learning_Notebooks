
from django.shortcuts import render
from datetime import datetime


# Puedo incluir Una serie de post de prueba
posts =  [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    }
]
# Crearemos los posts existentes, una lista


def list_posts(request):
    """List existing posts. Crea un HTML a partir de los post en posts
    Esto es solo un ejemplo, no es la forma apropiada. Se usa notaicón de Kwargs, para desempaquetar todo el 
    diccionario de posts en el .format


    """
    return render(request, 'feed.html', {'posts':posts})