<h1 align="center">
  <img src="Assets/logo_me.png">
  <br/>
  Project: News_Scraper
  <br>
</h1>


<h4 align="center">Fundamentos de Web Scraping con Python y Xpath en <a href="https://platzi.com/r/alejandro-sin/" target="_blank">Platzi</a>.</h4>
<p align="center">
  <a href="http://makeapullrequest.com">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="PRs Welcome">
    </a>
  <a href="https://github.com/Alejandro-sin?tab=followers">
    <img src="https://img.shields.io/github/followers/Alejandro-sin?tab=followers?style=social">
  </a>
  <a href="#mortarproyecto-scraper-de-noticias">
    <img src="https://img.shields.io/badge/Proyecto-brightgreen.svg?style=flat-square">
  </a>
   <a href="https://github.com/Alejandro-sin/Learning_WebScraping">
    <img src="https://img.shields.io/badge/Learning_WebScraping-brightblue.svg?style=flat-square">
  </a>
     <a href="https://twitter.com/Alejandrosin_" >
    <img alt="Twitter URL" src="https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Ftwitter.com%2FAlejandrosin_">
  </a>
</p>


---

## **LECTURAS MAESTRAS** :
- [Fundamentos de Web scraping y Xpath](https://platzi.com/cursos/web-scraping/)
- [Resumen maestro del curso en Notion](https://www.notion.so/Notas_Web_scraping-b69e6ab9c605462786f2fa380c2fb42d)
- [Xpath-W3](https://www.w3.org/TR/1999/REC-xpath-19991116/)
- [Wiki](https://en.wikipedia.org/wiki/Web_scraping)
- [Why webscraping?](https://www.octoparse.com/blog/why-web-scraping-may-benefit-your-business)
- [Xpath Cheat Sheet](https://devhints.io/xpath)

## **ARCHITECTURE** :

<ul>
        <li> <a href="#wall-web-scraping">Wall: Web Scraping</a></li>
        <li> <a href="#brick-introducción-webscraping-y-xpath">Brick: Introducción webscraping y xpath</a></li>
        <li> <a href="#brick-fundamentos-de-la-web">Brick: Fundamentos de la WEB</a></li>
        <li> <a href="#xpath">Brick: Xpath</a></li>
        <li> <a href="#mortarproyecto-scraper-de-noticias">Project: News-Scraper </a></li>
    </ul>

■________________________________________________________________ set() ■

## **WALL: Web Scraping**

■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

El web scraping es la extracción de datos de una página web vía código sin necesidad de acceder a una API.
El proyecto final de este aprendizaje es:

- Crear un Script para almacenar diariamente las noticias de cualquier página web. 
En este curso utilizaremos un periódico colombiano que servirá para futuros análisis de datos o 
desarrollo de aplicaciones web mediante: Xpath, Request, lxml, python


## **BRICK: Introducción webscraping y xpath**

■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

- **Web scraping** Es una técnica usada por data scientist y backend developers para extraer información de internet,
 accede a esto usando el protocolo de tranferencias de hipertexto (HTTP) o a través de un navegador. Los datos extraídos usualmente son guardados en una 
base de datos, incluso en una hoja de cálculo para posteriores análisis. 
Puede hacerse de manera automática (bot) o manualmente.

- **Xpath**  es un lenguaje que sirve para apuntar a las partes de un documento XML. 
Xpath modela un documento XML como un árbol de nodos. Existen diferentes tipos de nodos: elementos, atributos, texto.


### **CHUNK: ¿Por qué aprender web scraping hoy?**

■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


Las agencias de seguridad, aplicaciones que comparan precios más baratos entre hoteles, apliaciones de ecommerce que comparan
precios entre diferentes competidores usan web scraping.
Las agencias de marketing  para analziar el contenido de tweets que se vuelven virales. En general el web scraping es una habilidad muy valiosa
para cuando no tienes acceso a una API.

Es posible realizar web scraping con diferentes lenguajes de programación, como R o Js ( y sus respectivas librerías)
sin embargo Py es por excelencia el lenguaje de programación para esta tarea. Cuenta con la comunidad más grande para implementarlo. 

- [Más razones del porqué](https://www.octoparse.com/blog/why-web-scraping-may-benefit-your-business) Nota: Está en inglés, si estás en google y quieres leerlo
en español, haz click derecho/"traducir al español"


 
### **CHUNK: Python: el lenguaje más poderoso para extraer datos**

■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


- [Request](https://requests.readthedocs.io/es/latest/)

Es una librería nos permite controlar HTTP. El conjunto de reglas o protocolos de comunicación. En el enlace está la documentación en 
español plano.


> "El gobierno de su Majestad, Amazon, Google, Twilio, Mozilla, Heroku, PayPal,
NPR, Obama for America, Transifex, Native Instruments, The Washington Post, Twitter, 
SoundClound, Kippt, Readability y algunas organizaciones Federales de los Estados Unidos de América utilizan Requests internamente. 
Ha sido descargado más de 8,000,000 de veces desde PyPI. " 


- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

Es una libería de pyhton qué nos sirve para extraer información HTML y XML. Recibe este nombre debido a un poema con el mismo nombre
 de Lewins Carroll en Alicia en el pais de la maravillas.

> "Beautiful Soup, so rich and green,
Waiting in a hot tureen!
Who for such dainties would not stoop?
Soup of the evening, beautiful Soup! "

- [Selenium](https://selenium-python.readthedocs.io/)

Podemos crear navegadores fantasmas para controlar sitios web de manera automática. Bots.


- [Scrapy](https://scrapy.org/)

Permite escribir reglas para extraer los datos, es extensible por diseño,
es rápido y simple. Es usado por el UK para recolectar datos de la población. 


**HERRAMIENTAS DE WEBSCRAPPING**

Los siguientes son soluciones que no necesitan codear,  y que en su mayoría tienen un propósito específico.
Enfocados  ecomerce o a funciones como tomar screenshots de PDFs. Automatizar y agendar actividades, y las soluciones están dadas
como pluggins en el navegador hasta servicios. 

- [ParseHub](https://parsehub.com/)
- [webscraper.io](https://www.webscraper.io/)


**LIBRERÍAS Y LENGUAJES**

- [Rvest](https://www.datanalytics.com/libro_r/web-scraping.html) Es una librería inspirada en Beautiful soup, diseñada para
cosechar y recolectar datos de HTML. Se usa en R studio.

- [Puppeteer](https://pptr.dev/) Es una librería de Js que puede usarse para 
diferentes propósitos entre los cuales el webscrapping es uno. 


■________________________________________________________________ break() ■

## **BRICK: Fundamentos de la WEB**

■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

**HTTP**: Hypertext Transfer Protocol
____ 
Conjunto de reglas por el cual dos computadores se comunican. Un cliente y un servidor. El cliente realiza peticiones a servidores.

Una petición se ve así:

```
# Request
GET / HTTP/1.1
Host: developer.mozilla.org  Accept-Language: fr

# Response  HTTP/1.1 200 OK
Date: Sat, 09 Oct 2010 14:28:02 GMT
Server: Apache
Last-Modified: Tue, 01 Dec 2009 20:18:22 GMT  ETag: "51142bc1-7449-479b075b2891b"
Accept-Ranges: bytes  Content-Length: 29769  Content-Type: text/html
<!DOCTYPE html... (here comes the 29769 bytes of the  requested web page)


```
____

**HEADERS**
Permiten al cliente y el servidor passar información adicional con un request o response HTTP.
Pueden agruparse en las siguientes categorías:


- **Generales** : Aplica para request y responses pero no tiene relación con la data transmitida en el cuerpo
- **Request** : Contienen más información acerca del recurso a ser fetch (extraer)
- **Response** : Contiene información adicional sobre respuestas. Como ubicación o el Server provider.
- **Entity** : Contien información acerca del recurso del cuerpo.


Existen muchas cabeceras o headers como:
- Accept
- Authorization
- Link
- Location
- Save-Data

Puedes consultar aquí toda la documentación sobre las [cabeceras o Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)

_______

**HTTP** nos permite transportar, HTML, CSS, webAPIs, Js. 
Y se vale de protcolos como IP, TCP, UDP para comunicarse con el servidor, mediante TLS se hace la encriptación
Y el DNS asigna nombres a direcciones IP.

![HTTP](Assets/HTTP.png)

### RAW: **STATUS CODE** 

Los estados son la forma en que el servidor da respuesta de las peticiones.

1. Respuestas informativas (100–199).
2. Respuestas satisfactorias (200–299).
3. Redirecciones (300–399).
4. Errores de los clientes (400–499).
5. Errores de los servidores (500–599).

La siguiente hace parte de la documentación de Mozilla:

[STATUS RESPONSE](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

_____

**MANEJO DE STATUS CODES**

Una opción rápida para manejarlas es usar la librería Request
```
Shell*

1. Abre un ambiente virtual.
2. En la carpeta de trabajo: pip install request

```
Luego en pyhton

```
## Una idea sobre el manejo de los status Code.

import requests

response_platzi = requests.get('https://api.platzi.com')
print(response_platzi)
# <Response [404]>

if response_platzi.status_code == 200:
    print("Aquí tienes lo que buscas")
elif response_platzi.status_code == 400:
    print("Ups, no puedo darte nada en el momento. Nosotros nunca paramos de mejorar <3")
    

```
Un artículo para profundizar en cómo manejar la librería request y como manejar los status code: 
[Request Tutorial](https://realpython.com/python-requests/#status-codes)



### **CHUNK: HTML**

■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

**HTML** es una lenguaje que permite definir la estructura de una página web.
Estrucutra, estilo, partes interactivas. En el contexto de webscraping HTML es muy importante

Etiquetas está encerrado en angle brakets.<>
Una etiqueta peude contener a otras etiquetas, las etiquetas tienen atributos.
Los atributos será crucial conocerlos porque con ellos podremos conectar el scraper para 
extraer información.

____

- [script](https://developer.mozilla.org/es/docs/Web/HTML/Elemento/script) Se utiliza para
insertar o hacer referencia a un script ejecutable dentro de un docuemnto HTML.

- [meta](https://es.wikipedia.org/wiki/Etiqueta_meta) aporta información extra al documento, metadatos como autor, título, fehca, palabras clave
es de suma importancia para el navegador.

- [iframe](https://developer.mozilla.org/es/docs/Web/HTML/Elemento/iframe) Puedo anidar un elemento HTML
sobre otro elemento.

____


### **CHUNK: Robots.txt**

■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

Los archivos [robots.txt](https://support.google.com/webmasters/answer/6062608?hl=es) exiten como una forma de administrar una página web.
proporciona información a los rastreadores de los buscadores sobre las páginas o los archivos que pueden solicitar o no de tu sitio web. 
Principalmente, se utiliza para evitar que tu sitio web se sobrecargue con solicitudes.
En el contexto de webscraping, le dice al scraper que puede y no extraer. Es decir hasta donde puede llegar. Ya que infrigir en la violación
de estas directivas peude acarrear un problema legal con el sitio web al que estamos scrapeando.


**Robots.txt**
Contiene entre otros elementos:

USER-AGENT: Identificadores de quienes acceden a tu sitio web, puede ser un archivo.py hasta un googlebot.

**DIRECTIVAS**

ALLOW: Utiliza esta directiva para permitir a los motores de búsqueda rastrear un subdirectorio o una página, incluso en un directorio que de otro modo no estaría permitido
DISALLOW: Utiliza esta directiva para indicar a los motores de búsqueda que no accedan a archivos y páginas que se encuentren bajo una ruta específica

Ejemplo:

```
url/robots.txt
Pro ejemplo:

# Robots.txt file from http://www.nasa.gov
#
# All robots will spider the domain

User-agent: *
Disallow: /worldbook/
Disallow: /offices/oce/llis/

```


Para conocer más información de [robots.txt](https://ahrefs.com/blog/es/robots-txt/).


■________________________________________________________________ break() ■

## **BRICK: XPATH**

■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

XML Xtensible markup lenguage.
Sirvio para definir interfaces, es un lenguaje de nodos o etiquetas.
Una técnica para extraer datos de allí es Xpath.

Es parecido a las expresiones regulares
[Xpath](https://www.w3.org/TR/1999/REC-xpath-19991116/) es a HTML lo que las REGEX son a un texto.
Es decir, Xpath es un lenguaje de patrones, expresiones que me permitirá extraer
datos de un HTML.

[Cheat Sheet](http://labs.timtom.ch/library-webscraping/extras/xpath-cheatsheet.md.pdf)


### **CHUNK: Tipos de nodos**

■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

Un nodo es lo mismo que la etiqueta y su contenido.
Un nodo puede contener a otros nodos.
En otras palabras Xpath nos permitirá navegar en los diferentes niveles de profundidad
deseados con el fin extraer información. Para describir los nodos y relaciones con Xpath se usan una 
sintaxis de ejes.

[Toscrape](http://toscrape.com/) es un sandbox para practicar.
 



### **CHUNK: Expresiones en Xpath**

■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

 / : Significa la raiz o root de todo el documento, tambien significa un salto entre nodos.
 Puedo navegar entre niveles
 
 // : Puedo ir por varios niveles en el esquema que cosntruimos.
 
Ejemplo: 
 
``` 
# Fuente de trabajo Quotes to Scrape:

url ="http://quotes.toscrape.com/"

#Quiero extraer el texto de mi nodo h1.

$x('//h1/a/text()').map(x => x.wholeText)
# Devuelve en consola: ["Quotes to Scrape"]


#La función map pertenece a Js y la estoy usando para que me muestre todo el texto de la 
selección de Xpath.

```

Existen otras expresiones

/.. : Acceder a todos los nodos padre de x nodo.
/@atribute_name : Me permite extraer atributos

```
#Estoy trayendo todos los atributos class de los nodos span.
$x('//span/@class')
```
Para ser específicos con los datos a extraer se usan predicados.


### **CHUNK: Predicados Xpath**

■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

- [predicado] :Para encontrar nuestra información debemos ser más especificos, para ello
sirve los predicados.

**Predicados** :

- n : Hace referencia al n elemento de la lista.
- last(): Al último elemento de la lista.
- @atribute_name : Al usarse como predicado me trae todos los nodos
que contienen este atributo
- @atribute_name="" : Al usarse como predicado me trae todos los nodos
que contienen este atributo, incluso el value de este atributo.

Ejemplos:

```
# Para extraer solo uno de los div del div container usamos un predicado

$x('/html/body/div/div[1]')
# Devuelve [div.row.header-box]

$x('//span[@class="text"]/text()').map(x=>x.wholeText)
# Devuelve (10) ["“The world as we have created it is a process of o…cannot be changed without changing our thinking.”", "“It is our choices, Harry, that show what we truly are, far more than our abilities.”", "“There are only two ways to live your life. One is… The other is as though everything is a miracle.”", "“The person, be it gentleman or lady, who has not …ure in a good novel, must be intolerably stupid.”", "“Imperfection is beauty, madness is genius and it'…be absolutely ridiculous than absolutely boring.”", "“Try not to become a man of success. Rather become a man of value.”", "“It is better to be hated for what you are than to be loved for what you are not.”", "“I have not failed. I've just found 10,000 ways that won't work.”", "“A woman is like a tea bag; you never know how strong it is until it's in hot water.”", "“A day without sunshine is like, you know, night.”"]

```



### **CHUNK:Operadores en Xpath**

■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

Hay una forma de filtrar más avanzada y es con operadores lógicos.

**Operadores lógicos en Xpath** :
Cabe notar que los operadores se están usando dentro del predicado.

- !=
- <>
- and
- or
- not

Ejemplo

```
#Usando el operador != diferente, le estoy diciendo que me
traiga todos los nodos span que tienen clase diferente a Texto.

$x('//span[@class!="text"]')

# Usando operador not me devuelve todos los nodos que no tienen
el atributo class.

$x('//span[not(@class)]'

```


### **CHUNK:Wildcards en Xpath**

■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

Son comodines que usamos cuando no tenemos claro lo que queremos extraer.

- /* : Con asterisco le estoy diciendo que me traiga todos los nodos inmediatamente después de la expresión.
- //* : En este caso le estoy diciendo que estoy saltando en todos los niveles en todas las direcciones.
- @*: Traer todos los atributos de todos los nodos
- /node() : Nos trae además de nodos el contenido, difiere de asterisco.

Ejemplo:

``` 
x('//span[@class="text" and @itemprop="text"]/node()').map(x => x.wholeText)
# Devuelve (10) ["“The world as we have created it is a process of o…cannot be changed without changing our thinking.”", "“It is our choices, Harry, that show what we truly are, far more than our abilities.”", "“There are only two ways to live your life. One is… The other is as though everything is a miracle.”", "“The person, be it gentleman or lady, who has not …ure in a good novel, must be intolerably stupid.”", "“Imperfection is beauty, madness is genius and it'…be absolutely ridiculous than absolutely boring.”", "“Try not to become a man of success. Rather become a man of value.”", "“It is better to be hated for what you are than to be loved for what you are not.”", "“I have not failed. I've just found 10,000 ways that won't work.”", "“A woman is like a tea bag; you never know how strong it is until it's in hot water.”", "“A day without sunshine is like, you know, night.”"]

```




### **CHUNK:In text Search**

■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

Para buscar cadenas de caracteres especificas dentro de un texto.
- start-with(."Texto a buscar"): Empezar con, el punto hace referencia al nodo actual.
```

$x('//small[@class="author" and starts-with(.,"A")]/text()').map(x => x.wholeText)
#Devuelve (4) ["Albert Einstein", "Albert Einstein", "Albert Einstein", "André Gide"]

```

- contains (., "Texto a buscar") : Sirve para llamar por el texto contenido en.

```
$x('//small[@class="author" and contains(., "g")]/text()').map(x => x.wholeText)
#Devuelve ["J.K. Rowling"]

```

Nota: Debido a las versiones del lenguaje Xpath en los navegadores
las funiones end-with y matches no están disponibles, pero una ve en código python corren sin problemas.

- end-with(.,""): Termina en.
- matches(.,""): Sirve para hacer una búsqueda en el texto de un nodo que coincida 
con una expresión regular.



### **CHUNK: Xpath Axes**

■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


Un eje representa una relación entre el nodo actual. Es usado
para localizar nodos relativos a el nodo en el DOM tree.

```
$x('/html/body/div/self::div')
$x('/html/body/div/descendant-or-self::div')

``` 

Para ver más: [Axes](https://www.w3schools.com/xml/xpath_axes.asp)




### **GRAFITTI**:
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


Una infografía brillante de [platzi](https://platzi.com/) para resumir este tema.


![Grafitti](Assets/XPath-Cheatsheet.png)






### **GLUE**:

■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
* Realizar expresiones Xpath para:


- Descripción:

``` 
$x('//article/p/text()').map(x => x.wholeText)
["It's hard to imagine a world without A Light in th…for you. Shel, you never sounded so good. ...more"]
```

- Stock

```
$x('//article[@class="product_page"]//p[@class="instock availability"]/text()').map(x=>x.wholeText)

```


- Precio

```
$x('//article[@class="product_pod"]/div[@class="product_price"]/p[@class="price_color"]/text()').map(x=>x.wholeText)
#Devuelve: (20) ["£51.77", "£53.74", "£50.10", "£47.82", "£54.23", "£22.65", "£33.34", "£17.93", "£22.60", "£52.15", "£13.99", "£20.66", "£17.46", "£52.29", "£35.02", "£57.25", "£23.88", "£37.59", "£51.33", "£45.17"]
```

- Barra lateral izquierda categorías:

```

$x('//div[@class="side_categories"]//a[@href]/text()').map(x=>x.wholeText)

```

## **RESUMEN:"Recordando"**

■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

En este curso aprendimos : 
 - Las bases fundamentales del webscraping y porqué es importante en la actualdiad.
    y porqué esta herramienta es útil conocerla y saberla usar como un backend o un data Scientist
 - El **web scraping** es uan actividad que se puede hacer en diferentes lenguajes de programación, y con distintas herramientas automatizables, ya sea
  desde código hasta pluggins de chrome.
 - **Revisar el robots.tx**t para saber siempre lo que está restringido por el usuario administrador, y así
no incurrir en problemas legales.
 - **Revisar legalidad** sobre extracción de datos del país donde pretendo realizar webscraping
 - Xpath Lenguage como un generador de patrones de búsqueda en un árbol del DOM. Es decir, un apuntador a un XML.
    > "*Xpath es a HTML como REGEX es a un documento de texto. Facundo Nicolás García Martoni*"
 - La variabilidad de las expresiones Xpath varían en función del recorrido que se tome en el HTML,
    en el sitio web como tal y sus desarrolladores, así como las visicitudes del tiempo.                                                                                                                      
 - **HTTP es un protocolo de comunicación** para la transferencia de información. Así habla el cliente y el servidor.
 - HTTP es un paquete que lleva consigo HTML, CSS, Js, Web APIs. Y el servidor da una respuesta numérica en un intervalo de (100-500) que son respuestas a sucesos con el servidor.
 Van desde la abnegación de información a la satisfación de la solicitud. 
 - Preparar el **ambiente de trabajo apropiado** en python es crucial, y lo aprendimos en diferentes OS, sobre Cmder en Windows
 y sobre las buenas prácticas de los ambientes virtuales.
 - Aprendimos las librerías  **Request, Lxml, Os,  datetime, autopep8**
 - Sobre manejo de errores, creación de archivos y carpetas en función de Noticias scrapeadas.
 - Utilizamos manejadores contextuales y desarrollamos un scraper robusto que colecta noticias del diario Colombiano **"la republica"**
 


### **MORTAR:Proyecto scraper de noticias**

■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

Este proyecto es un scraper de noticias del diario [la_Republica](https://www.larepublica.co/) Vamos a extraer de este periodico, encabezados y cuerpo de las noticias diariamente y almancenarlos para un posterior análisis. Como análisis de Texto, marketing, análisis de sentimientos y demás.
____

**Notas** :

- Observar https://www.larepublica.co/robots.txt para tener claro a qué podemos o no acceder con nuestro scraper

____

**Entorno de trabajo.**
- Es necesario tener buenas prácticas para desarrollar, en python como todo lenguaje tiene sus propias. A continuación la configuración de este proyecto.

(Window)

Es posible realizar estas acciones desde cualquier otro shell. En este curso se usa [Cmder](https://cmder.net/). **cmder** es un emulador de bash, a partir de los comandos nativos de windows generamos una "aliases" que tratan de igualar los comandos que tenemos en consola de tipo UNIX. En windows podríamos usar comandos más habituales para programar.


## **Pasos**

0 ■ Inicializamos git en el directorio de trabajo

```
git init

```

1 ■ Creamos nuestro ambiente virtual:

``` 
py -m venv venv (Windows)
python (linux) ... 

```

2 ■  Creamos en el directorio de trabajo o carpeta un archivo .gitignore y escribimos que ignore  la carpeta del ambiente virtual. No queremos ocupar espacio innecesario y no es buena práctica.

```
(.gitignore)

venv/
(nombre de la carpeta que vamos a ignorar)/

```
3 ■ Para activar el ambiente virtual realizamos

```
ven\Scripts\activate (Windows)
source venv/bin/activate (Linux)

```
4 ■ Si trabajas en VsCode. Creamos un Workspace para tener una estructura más organizada "save as workspace" y así tener un workspace para que VS tenga idea de qué tenemos en esta capeta.

5 ■ Instalamos las dependencias de este proyecto:
1.  Request: Para realizar peticiones
2.  Lxml: Para utilizar Xpath
3.  Autopep8: Ayuda a formatear el código según los estilos oficiales dle lenguaej,e

```
pip install request lxml autopep8

```
Es buena práctica tener actualizado el manejador de paquetes de python.
```

py - m pip install pip --upragade

```

### **PAINT:Desarrollo proyecto**

■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

Construimos expresiones Xpath para las los titulos, links, resumen y cuerpo.

Las expresiones Xpath pueden variar en función del sitio web y los desarrolladores.
Por lo que las expresiones debe estar en constante revisión. 

1. Crear un archivo xpath.txt para almacenar las expresiones que corresponden.

2. Obtener todos los links con python.

3. Guardando las noticias en archivos de texto.

Vamos a realizar una lógica para ir de cada link al sitio de cada noticia
y de ahí extraer:

- Titulo
- Resumen
- Cuerpo




■________________________________________________________________ exit() ■
