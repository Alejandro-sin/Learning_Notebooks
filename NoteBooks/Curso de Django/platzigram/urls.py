'''
Módulo de URL de python
'''
from django.contrib import admin
from django.urls import path
from platzigram import views as local_views
# Importamos las vistas de posts
from posts import views as posts_views


urlpatterns = [

    path('hello-world/', local_views.hello_world),
    path('another/', local_views.another),
    path('auth/<str:name>/<int:age>/', local_views.auth),
    path('posts/', posts_views.list_posts)

]
