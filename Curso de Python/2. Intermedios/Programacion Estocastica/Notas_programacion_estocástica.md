
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
#    **WALL:**
******************************************************
* LECTURAS MAESTRAS:
    + https://en.wikipedia.org/wiki/Stochastic_programming
    
* RESUMEN MAESTRO:
* GLOSARIO UNIVERSAL DE TÉRMINOS:
* ATAJOS:

##   **BRICK: Programación Dinámica**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
###    **NOTAS:**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

###    **CHUNK:**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■



**CONCEPTO: Core** 
_________________________________________________
El nombre no tiene nada que ver con la técnica.
Richard Bellman usó el nombre de programación se escogió para escocnder a los patrocinadores gubernamentales el ehcho de que estuviera trabajando con matemáticas.

Es muy poderosa para optimizar un cierot tipo de problemas


Subestructura óptima:
La solición óptima global se puede encontrarndo  soluciones optimas a problemas locas.
Encontrar solucioens a problemas pequeños.

Problemas empalmados.
Fibonacci solución recursiva tradicional. Problemas empalmados, solucionamos una y otra vez el mismo problema,


Memoization

La Memrorización es una técncia para guardar cómputos previos y evitar realizarlos nuevamente.

Normalmente se utiliza un diccionario, donde las consultas s epueden hacer en o(1), puedo consultar mis resultados en un diccionario de manera eficiente
Al guardar los resultados en memoria nos ahorramos tiempo de cómputo, "Intercambia tiempo por espacio."




**CONCEPTO: Optimización de Fibonacci.** 
_________________________________________________

Adentrarme en el mundo de las sucesiones.
https://es.wikipedia.org/wiki/Sucesi%C3%B3n_de_Fibonacci
https://www.youtube.com/watch?v=yDyMSliKsxI
https://www.youtube.com/watch?v=WmQrzrGhVC4

**CONCEPTO: Caminos aleatorios** 
_________________________________________________
Deterministas: Al mismo input obtenemos el mismo outpu. Todo lo escrito hasta aquí ha sido así.

* Es un tipo de simulación que elige aleatoriamente una desición dentro de un conjunto de descioens válidas.

Se utiliza en muchso campos del conocimeindo cuando lossistemas no son deterministas e inclyen elementos de aleatorieadd.

Tieen limitacioens apra algunos problemas.
Muchos problemas son de contexto random, ¿Como los incorporo?
Caminos aleatorios, elegir dentro d eun set, aleatoriamente, a através de desiciones probabilisticas.

No determinista: Cada vez que tenemos un input tenemos un resultado proable.

El movimiento browniano, definido por Eistein, a través de la aleatoreidad.
El moviiento atómico es aleatorio que tiene representaciones macroscópicas.
Simulaciones de partículas. Se determina el caso base, y se multiplica por miles d ecaminos aleatorios.
Las simulacioens de colisiones y mezcla de galaxias, como la nuestra.
 Mercados financieros, laas acciones son caminos aleatorios.
 
 En londres, está el Cuantum cloud Scultputre.
 FOrmó un camino aleatorio computacional qu edio como resultado una estructura.
 
 Pollock y la programación?
 
 ¿ Que sistemas aleatorios existen y en cuales puedo tener un conjutno de reglas que me permtian simular las cosas?
 
 ¿ Cómo puedo medir el desorden ?


https://en.wikipedia.org/wiki/Entropy_(information_theory)
https://en.wikipedia.org/wiki/R%C3%A9nyi_entropy
https://en.wikipedia.org/wiki/Conditional_entropy
https://en.wikipedia.org/wiki/Entropy_(computing)

** Buscar ilustaciones con programación aleatoria. Codigo fuente
** Puedo mezclar el desorden y el orden?
Es decir, peudo decirle a un program que me ejecute desorden cada x movimiento y que cada y veces se repita una forma de patrón?
Es dcir, puedo hacer patrones aleatorios? Qeué sucede cuadno se encuentran los dos?


**CONCEPTO:Introducción a la Programación Estocástica** 
_________________________________________________

Un programa es deterministico si al recibir un input reccibe el mismo ouput, 
La programación  estocásticas se aprovechan que las distribuciones probabilisticas de un problema se conocen o pueden ser estimadas.
Simulaciones, físcias, financieras,  se usa para entender difernetes comportamiento de medicamentos, para hacer autos autónomos.

Si tenemos datos estadísticos de la intersección d eun tráfico, podemos probabilisticamente cuando tenemos que prender un semafor en verde,
o en rojo. Un programa que se adapta a la situación.

La forma en la que vemos el problema es el que genera el tipo de solución.
Para eso hay qu econocer la población.

También podemos usar la inferencia estad´sitica. Que podemos incorpor a nuestras soluciones.
¿Cuando un problema es mejro resolverlo deterministicamente?
¿Cuando un problema es mejor resolverlo estocásticmaente?

**CONCEPTO: Cálculo de Probabilidades** 
_________________________________________________

Probabilidades.

* La probabildiad es una medida de la certidumbre asiciada a un evento o suceso futuro y suele expresarse como un número
 entre 0 y 1.
 
 Una probabilidad de 0 siginifica que un sucedo jamás sucederá.
 
 Una probabilidad de 1 significa que un sucese está garantizado de suceder en el futuro.
 
 Qué fracción de todos los posibles eventos tiene la propiedad que buscamos.
    Brute Force(Enumeración exhaustiva)
 
 Es importante calcular las posibilidades de un eventos para entender su probabilidad.
 
 La probabilidad de que un evento suceda y de que no suceda es siempre de 1.(El ser no admite ambiguedades)
 
 
 Pa + P-a=1 Ley del complemento
 
 + Ley multiplicativa, la probabilidad de que un evento suceda y otro suceda.
   regla general. El producto de probabilidades siempre es menor que las probabilidades individuales de ocurrencia.
        P(ayb) = Pa*Pb  
 
 - Ley aditiva.
    La probabilidad de hacer do
    Pa o b = Pa +PB mutuamente exclusivos
    Pa o b = Pa +Pb -P(AyB) No exclusivos  
 
 
 y siginifica priductpo 
 o significa sumar


**CONCEPTO Inferencia Estadística** 
_________________________________________________
Con simulaciones podemos calcular las probabilidades de eentos complejos sabiendo las probabilidades de eventos simples.

¿Que pasa cuando no concoemso la probabilidad de eventos simples?

Las técncias de inferencia estadísticanos permiten inferir/concluir las propeidades de
una población a partir de una muestra aleatoria.


* Una muestra aleatoria tiene a exhibir las mismas propeidades que la población de cual fue extraída.Jhon Guttag
(Somos una aberración estadística?)

=> Estio anteior sucede pro la Ley de los grandes números.
    Conforme generamos más pruebas, la probabilidad de las pruebas tiene a cero, o a la probabilidad real.
    La media de las muestras confome se reptinen tiende a 1

Para  hace runa inferencia primero debemos medir la media.

* La media es uan medida de tendencia centra
* Comunmente es conocida como el promedio

el segudno paso para inferir es calcular la varianza yla desviación.

Varianza y desviación estándar son medidas de propagación.

+ La varianza mide qué tan propagados se encuentran un conjunto de valores aleatorios de su media.
+ Mientras que al media nos da una idea de dónde se encuentran los varlores la variabza nos dice que tan dispersos están
+ lA VARIABZA SIEMPER DEBE ENTENDERSE CON RESPECTO A LA MEDIA.
Da unidasd cruadadas-


Desviación estándar.
Raiz cuadrada de la variazan. Nos permtie hablar de la variabildiad en potencias de 1.
La desviación estándar está en las mismas undiades que la media

Mostrar gráficos de dispersión.


**CONCEPTO: La Falacia del apostador** 
_________________________________________________
La falacia del apostador señala que después de un evento extremo, ocurrirán eventos menos extremos para nivelar la media.
Cada evento es independiente.
Pero si sucede...
La regresión a la media señala que después d eun eventos aleatorio extremo, el siguiente evento probablemente será menos extremo.
Después de que tire 20 6, la probabilidad que tire 6 es menos probable.


**CONCEPTO: Distribución Normal** 
_________________________________________________
 Distribución recurrente.
 Definida completamente por la media y su desviación estándar
 Permtie calcular intervalos de confianza con la regla empirica


La variabildiad de los datos es directamente proporcional a la desviación estándar.
A mayor variabilidad mayor desviación estándar.

La desviación estándar te da el riesgo de las inversiones. respecto a la media de la ganancia.

La regla empírica se conoce como:
Analizar la distribución dentro de na distriución.
la regla del 68-95-99,7 %
Señala cual es la dispersión de los datos en una distribución normal a uno dos y tres sigmas.
Permite calcular las probabilidades con la densidad de distribución nomal.

UN evento sucede con x probaildiad +- su intervalo de confianza.




**CONCEPTO:¿Qué son las Simulaciones de Montecarlo?** 
_________________________________________________
Stanislao Ulam, Von Neuman y el solitario, se llaman asi porque las priemras siulacioens al azar fueron sobre el casi MonteCarlo
Las simulaciones sirvieron para el proyecto Manhatam

Utilizan la aleatoriedad para generar un rporblema.

+ Permite crear simulacioens para predecir el resultado de un problema
+ Pemite convertir problemas deterministcis en problemas estocasticos
+ Es utilizado en una gran diversidad de áreas desde biología a derecho.


Calulcar Pi.

Simulaciones de Buffon y lapclae, caluclo de pi mediante probabilidades.
Buscar más.

Al generar inferencias estadíticas y le aplicamos los métodos.
Nos acercamos con cada iteracción a una conclusión estádisticamente válida que es diferente a una conclusión válida.

Significa que si iteramos n veces, nos vamos a acercar a +- una desvición de una media dada.




**CONCEPTO: Muestreo e intervalos de confianza** 
_________________________________________________

Es imoprtante cuando no tenemos la capcidad computacional de calcular todala población
Las muestras tienen a exibir las mismas propeidades de la población objetivo.

El tipo de muestreo probabilistico.
+ Muestreo aleatorio, cualquiero miembro de la poblacion tenga la misma probabildiad de ser escogido.
+ Muestreo estratificado tomams las caracterstica de la población para partirla en subgrupos y luego comomaos las muestras de cada subgrupo.
    Sirve para no sesgar muestras.
    Incrementa la probabilidad de queel muestroe sea representativo de la población.
    



Como se hace el muestroe de datos?





**CONCEPTO:Teorema del límite central.** 
________________________________________________
http://195.134.76.37/applets/AppletCentralLimit/Appl_CentralLimit2.html

Este teorema permite convertir distribuciones de x tipo en la normal.

Establece que muestras de cualquier distribución van a tener una distribución normal.
Permite entender cualquier distribución como la distribución normal de sus medias y eso nos 
permite aplicar todo lo que funciona en distribcuines

https://es.wikipedia.org/wiki/Teorema_del_l%C3%ADmite_central

¿Puedo hacer un algoritmo de ordenamiento al azar?
Osea cómo aplico el teorema de límite central en el ordenamiento binario?




**CONCEPTO: Cómo trabajar con datos experimentales.** 
_________________________________________________
Regresion lineal sirve para confirmar el grado  de confianza que podemos hacer sobre una teoría.
Nos permite aproximar una función a un conjunto de datos obtenidos de manera experimental
No necesariemtne permite aproximar funciones lineales, sino que sus variantes permiten aproximar cualquier función polinómica.




Una hipótesis
Basado en esta se crea un experimento para calidar o falsear la hipótesis
Se validda o falsea midiendo la diferencia entre las mediciones experimentales y aquellas mediciones predichas por la hipótesis.


**CONCEPTO:** 
_________________________________________________


**CONCEPTO:** 
_________________________________________________















■________________________________________________________________ break() ■





♀#### **PREGUNTAS:**
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
La librería "random" de Python nos otorga el siguiente método
d NO-->e

Py se calcula solo mendieante dividir circunfrencia / radio

d Circunferencias montercarlo

Es posible convertir cualquier distribución en una distribución normal
e

Para describir una distribución normal únicamente necesitamos de la media y de la desviación estándar
c NO-> d

La probabilidad es una medida de certidumbre que tenemos sobre si un evento futuro sucederá o no
c NO -->e

Una muestra aleatoria tiende a exhibir las mismas propiedades que la población de la cual fue extraída
b

¿Cuándo debemos hacer muestreo?
c

La probabilidad de que estés estudiando en Platzi y de que seas Colombiano es menor a la probabilidad de que seas Colombiano
d

El muestreo estratificado divide la población en subgrupos para no sesgar la muestra
b

Si corremos un programa de caminos aleatorios siempre vamos a obtener la misma visualización
b


La regresión lineal únicamente funciona con líneas
b


¿Qué son los programas deterministas?
e

La Desviación Estándar es una medida de dispersión
a

Para cada simulación que queramos escribir siempre existe una respuesta correcta sobre si el programa debe ser estocástico o determinístico
d

Podemos hacer regresiones lineales con la función de numpy "np.polyfit"
verdadero

Los programas estocásticos nos permiten modelar fenómenos aleatorios
d


Podemos utilizar simulaciones de Montecarlo para encontrar probabilidades de obtener diferentes tipos de manos de barajas
e


¿Por qué memoization funcionó para optimizar el algoritmo de Fibonacci?
b

Los caminos aleatorios se pueden utilizar únicamente en el mundo de la Física
e

La media es una medida de tendencia central
e

Las simulaciones de Montecarlo únicamente pueden ser utilizadas en juegos de azar
d

¿Qué es el camino de borrachos?
d

Siempre se deben obtener datos antes de plantear una hipótesis
e NO --> c

La única forma de calcular PI es dividir la circumferencia entre el diametro
d

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
