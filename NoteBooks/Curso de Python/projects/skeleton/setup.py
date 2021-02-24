'''

Sirve para crear un setup y mirar si quiero instalar mi proyecto después.


Buscar esos módulos.

setuptools
distutils.core
'''


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config ={
    'description':' My proyect',
    'author':'My Name',
    'url':' URL to get it at',
    'download_url':"Where to down...",
    'author_email':"my mail",
    'version':'0.1',
    'install_requires':['nose'],
    'packages':['NAME'],
    'scripts':[],
    'name':'projectname'
}

setup(**config)