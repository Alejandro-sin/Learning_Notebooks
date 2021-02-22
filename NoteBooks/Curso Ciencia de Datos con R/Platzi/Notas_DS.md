
# **Indice**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


+ [Hipervínculo](url)
 + + [Hipervínculo](url)
+ [Hipervínculo](url)
+ + + [Hipervínculo](url)
+ + +  [Hipervínculo](url)
+ [Hipervínculo](url)

■________________________________________________________________ set() ■





******************************************************
#    **WALL: Curso Profesional en ciencia de datos**
******************************************************
* LECTURAS MAESTRAS:
* RESUMEN MAESTRO:
* GLOSARIO UNIVERSAL DE TÉRMINOS:
* ATAJOS:
https://datascienceplus.com/missing-values-in-r/


###    **NOTAS:**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


##   **BRICK:Introducción Mundo Data Science**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
###    **CHUNK: DS**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

Bienvenido al curso Profesional de Ciencia de Datos, en este curso la profesora Inés Huertas experta en Big data e inteligencia artificial te va a enseñar:
Breve introducción a R
Web scrapping
Visualización de datos
Operación de datos
Transformación de datos
Exponer los datos a través de un API
El mundo del data science no es algo nuevo, desde los años 60 existían los mineros de datos: Personas dedicadas a analizar grandes cantidades de datos con estadística. Los mineros de datos tenían una limitante tecnológica pues demasiados datos eran difíciles de procesar, hoy en día gracias a toda la mejora en el hardware es que el mundo de data science se ha expandido.
El trabajo de un data scientist lleva varios pasos:
Obtención de datos.
Enriquecimiento de los datos.
Adecuación e interpretación de datos.
Aplicación del modelo.
Interpretación de los resultados.
Puesta en producción del modelo.
Existian minero de datos, evolucionaron por hardware para procesar nuevas cosas.
DS también es enriquecer los datos.
El trabajo como DS
Obteneción Enrquicemiento
Adecuación e interpretación de datos.
Aplicación del modelo
Interpretación de los resultados
Puesta en producción del modelo.


###    **CHUNK:¿Qué hace un Data Scientist?**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

Un data scientist es el encargado en una organización que busca encontrar verdades a través del análisis masivo de datos para poder guiar al equipo en la toma de decisiones
El flujo de trabajo de data un data science tiene muchos factores que deben ser tomados en cuenta.

En esta clase aprenderás lo que hace un data scientist a través del flujo de vida de un proceso profesional de data science, este proceso lo aprenderás en nuestro curso de Data Science.

Flujo profesional de un DS
___________________________

1. Entendimiento del negocio-> adquisición de datos-> Deployment ->Modeling
Entender que vendo, como lo llevo al mercado.
Que patrones de datos son importante sy como lso obtengo, luego los limpio. Datos basura de entrada resutlados basurao.
    La fuente d elso datos
    Recorrid
    La frecuencia
    La limpeiza y dodne viven
Luego modelamso según nuestros fetrues puntuales. Qué datos nos permtien tener respuestas? Que tipo de x debería hacer más? Mas o menos.

Interpretación de datos en modeling, podemos hacer le modelo matemático.

Cross Validatiom, Muestreamos datos y le pasamos datos.
La calificación nos permite hacer que tan acertado es neustro modelo.

Se iteran los procesos donde hagan falta.

Luego se lleva a deployement.
    Condiciones cambiantes del negocio hacen cambiar mi proceso de DS

###    **CHUNK: Introducción a R**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

R es un lenguaje de programación para aplicar técnicas estadísticas a un conjunto de datos. Para instalarlo debemos ir a su sitio en cran.r-project.org y seguir los pasos de instalación de nuestro sistema operativo.

Una vez instalado ya podremos ejecutar dentro de nuestro shell código de R, pero para mejorar nuestra experiencia al desarrollar vamos a descargar RStudio.

Para instalar librerias dentro de R solamente ejecutamos el comando install.packages(). Dentro de RStudio también contamos con una pestaña que nos va a mostrar las librerías que tengamos disponibles y cargadas en el proyecto.

install Spatial

Visualizaciones
https://www.r-graph-gallery.com/cartogram

## Presentación del proyecto
Para este curso vamos a realizar:

Obtener los datos de productos en Amazon para almacenarlos en dataframes.
Aplicar K-means a nuestro conjunto de datos para identificar clusters de productos.
Servir nuestro modelo de datos en una API Web.
Usar Shiny para interactuar con los datos.


###    **CHUNK:WebScripoing con R**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
###    **CHUNK:**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
###    **CHUNK:**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
###    **CHUNK:**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
###    **CHUNK:**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■



###    **BRICK:Web Scrapping**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
###    **BRICK:Adecuación y Análisis descriptivo de los datos**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
###    **BRICK:Aplicando modelo no supervisado: Kmeans**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
###    **BRICK:Modelo en producción**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
###    **BRICK:Representación de los resultados del modelo**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■




_________________________________________________
**CONCEPTO** :
_________________________________________________



_________________________________________________
**CONCEPTO** :
_________________________________________________

_________________________________________________
**CONCEPTO** :
_________________________________________________

_________________________________________________
**CONCEPTO** :
_________________________________________________

_________________________________________________
**CONCEPTO** :
_________________________________________________

_________________________________________________
**CONCEPTO** :
_________________________________________________

_________________________________________________
**CONCEPTO** :
_________________________________________________

_________________________________________________
**CONCEPTO** :
_________________________________________________

_________________________________________________
**CONCEPTO** :
_________________________________________________

_________________________________________________
**CONCEPTO** :
_________________________________________________














■________________________________________________________________ break() ■





#### **PREGUNTAS:**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■




* 
* 
* 


■________________________________________________________________ break() ■

#### **RESUMEN PARCIAL**:
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
```
<code>

```



■________________________________________________________________ break() ■
## EXÁMEN:
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

■________________________________________________________________ break() ■
#### **REFERENCIAS INTERESANTES**:
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

+ [Hipervínculo](url)
+ [Hipervínculo](url)
+ [Hipervínculo](url)
+ [Hipervínculo](url)
+ [Hipervínculo](url)
+ [Hipervínculo](url)

■________________________________________________________________ exit() ■
