
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
#    **WALL: Porgramación probabilistica**
******************************************************
* LECTURAS MAESTRAS:
    + https://en.wikipedia.org/wiki/Probabilistic_programming
* RESUMEN MAESTRO:
* GLOSARIO UNIVERSAL DE TÉRMINOS:
* ATAJOS:

##   **BRICK:Introducción a la probabilidad**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
###    **NOTAS:**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
Esta parte que llvo es la parte solo la introductoria.

###    **CHUNK: Probabilidad condicional**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
La probabilidad es cuanto sucede un evento sobre la totalidad de eventos posibles.
Los juegos de cartas, sacar una carta... porobilidad independiente, los evenots no están relacionados unos con otros.

Las probabildiadas condicionales toman en condieración el eento anterior. Para ahcerlo usamso el dado que o pipe

Uso estas formuals cuadno veo que algo no es indepndiente  depende la ocurrencia de un evento, de otro. |
P(ayb)= p(a) p(b|a)


p(b) =p(a) p(b|a) + p(~a)p(b|a)


_________________________________________________
**CONCEPTO:p(b) = p(a) p(b|a) + p(~a)p(b|~a) ** 

La proabialdiad de b es la suma de los eventos quesi son mas los que no son, se toma en consideración todo el universo.
Pcancer= p.positivo*(p.cancer| positivo) + p.negativo*(p.cancer| negativo)
Cual es la probabilidad de tener en un resultado cancer = a pa probabildidad de cancer por esta probabildiad dado que sea positivo más el negativo 
de la probabilidad de tenerlo.

_________________________________________________


###    **CHUNK: Teorema de Bayes**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
Thomas Bayes, se genera un albacea literio, Richard Price 1763 se encontró por la pregunta de Bayes. Que nos permitía incorporar evidnecia
para aproximarnos el pensameinto de proabilidad.

_________________________________________________
**CONCEPTO: ** 

La proababildiad de una hipotesis a dada alguna evidencia/evento b 

p a|b = (p (a|b)* p(a))  / p(b) y como p(b) = p(a) p(b|a) + p(~a)p(b|~a)

=> p a|b = (p (a|b)* p(a))  / p(a) p(b|a) + p(~a)p(b|~a)

De que la hipoteisi y el evento en conjunto  /sobre la probabilidad de cierta evidencia.

p(a) es prior, cual es la hipñotesis antes de recolectar evidencia.
p(a|b) = una vez la evidencia, como las actualizamos?

Eicosograma, es el rectángulo el espacio seccionado que se interpretan valores.
(Buscar más) Eicosograma para ver proporciones probabilsiticas.
_________________________________________________
La probabildiad no necesariamente es la matematica de la aleatoriedad
La probabilidad es la matemática de las proporciones, penssar proporciones, cuanteas veces espero ver algo dentro las totalidad de lo que va a suceder.
La visualización nos permite desarrollar pensamiento proabilistico.


Buscar como aprende ra visualziar abstracciones matemáticas para poder dimensionar las cosas.

_______
https://www.youtube.com/watch?v=HZGCoVF3YvM&t=393s
https://www.youtube.com/watch?v=CP4ToX5Tyvw
_________________________________________________


###    **CHUNK: Análisis de síntomas**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

A continuación se realizará con teorema de Bayes el diganóstico de un paciente.


# dETERMINAR IS MI HIPOTESIS ES CIERTA O NO Y CON QUÉ GRADO DE PROBABILDIAD. Aqui se actualiza nuevamente la información.
# Podemos hacer el ejercicio para el CODVID, ejemplo util:
https://platzi.com/comentario/1304968/



nos permite medir nuestra certidumbre con respecto a un suceso tomando en cuenta nuestro conocimiento previo y la 
evidencia que tenemos a nuestra disposición.
https://platzi.com/clases/1841-probabilistica/26581-aplicaciones-del-teorema-de-bayes/ Ejemplos
cita del famoso economista John Maynard Keynes que resume perfectamente el tipo de pensamiento que quiero que desarrolles:
 “Cuando los hechos cambian, yo cambio mi opinión. ¿Qué hace usted, señor?”


###    **CHUNK:Garbage in, garbage out**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
Nos va a permitir identificar errores aun cuando nuestro computo sea es correcto
como una tercera capa de errores, existen de sintaxis, de lógica, y estos ultimos son diseño, la forma en la que pensamos
que nos llevan al error.

+ GIGO garbage in Garbage out.

La calida de nuesrtos datos es igual de fundamental que la precisión de nuestros cómputos
Cuando los datos son errados, auqneu tengamos un cómputo impecable, nuestros resultados serán erróneos.
Con datos errados las conclusiones serán erradas.

El censo de 1840 en EEUU manual

https://es.qwe.wiki/wiki/1840_United_States_Census



###    **CHUNK:Imágenes engañosas**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
Extrapolar anticipadamente antes de ver una imagen.
Se puede llegar  a conclusiones erróneas.
Las imageens son importantes apra entender conjunto de datos.
No confiar graficas sin escalas o etiquetas.



###    **CHUNK:Cum Hoc Ergo Propter Hoc**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
https://es.wikipedia.org/wiki/Cum_hoc_ergo_propter_hoc

Correlación no significa causalidad.
Correlacción significa que dos variables se mueven en:
+ la misma diracción
- direfente sifercion.

Despues de esto, eso, entocnes a consecuecia de esto, eso.
.
¿Que otra cosa hay detrás de lo que observo?

Si eñ niño ve violencia es vioento?

Edad media piojos eran beneficioso, las personas saludables tenían piojos.
Piosios sensibles a la temperatura del cuerpo, al no tener el ambietne adecuado, desaparecen.
Los piojos eran buenos para la saluda.

En todo lo que peinso que existe causalidad uqe no estoy voendo?



###    **CHUNK:Prejuicio en el muestreo**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
Para que una muestra pueda servir como base de inferencia estad´sitica tiene que ser aleatorio y representativo.
El prejuicio en el muestro elimina a repersentativivdad d elas muestras.
A veces conseguir muestras es difícil, por lo que se utiliza a la población de más fácil acces.

 

###    **CHUNK:Falacia del francotirador de Texas**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

Se ca cuado No tomamos la aleatoreidad en consideración,
    El no tener encuenta evento aleatorios.
Cuando nos enfocamos en las imilitudes e ignora las diferencias.
    Buscar Similutdes relevantes.
Cuando fallasmos al tener una hipótesisi antes de recolectar datos estamos en alto riesgo de caer en esta falacia. (COmun en DS)
    
    No puedes sacar hipótesis sin datos.
    

###    **CHUNK:Porcentajes confusos**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

Cuando no sabemos la cuenta total del cual se obtiene un poercetaje tenemos el riesgo de concluir falsos resultados.
Siempre es importante ver el contexto
Los porcentajes en vaciío no significan mucho
Datos correcto, programa correcto, conclusiones correcto.


###    **CHUNK:Falacia de regresión**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

Muchos eventos fluctuan naturalemte, la temerpatura, el rendimiento d eun atleta, rendimiento porfatolio de invresion
La flutcuation peude recibir medidas correctias, se puede creer que existe un vínculo de una causalidad en 
lugra de una regresión a la media.

Después de un evento extremo regresamso a la normalidda de los eventos.
Pensar que la medida correctiva es la causa de regresar a la media e sun error de una Falacia
Tiene que ver cuando un evento fluctua naturalmente y regresa a la media.


Leer las tendncis ante sde implementar soluciones.
Entender caudno aplciar el principio,  

https://es.wikipedia.org/wiki/Anexo:Sesgos_cognitivos





###    **CHUNK:Introducción a Machine Learning**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
Esel campo de estudio que le da a las computadoras la habildiad de aprender sin ser explícitamente programdas.

Marvin Misnky la primera red neurnal.

Los humanos memorizamos y generalizamos


Perceptron, reonocia digitios escritos a mnao.
Red aversarial. Jugar apra automatizar las regals de un juego.

Nearest Neibor. para detectar patrones de datos que prexisten. Calcular turtas de ciduades cercanas.
DeepBlue le gaó a Gasparov.
Fei FEI and IA.


Machien learning se utiliza cuando programar un algorimto es imposible.
eL PROBLEMA ES MUY COMPLEJO O NO SE CONOCEN ALGORITMOS PARA RESOLVERLO.
aYUDA A LOS HUMANOS A ENTENDER PATRONES. dATA MINING.

Aprendizaje supervisado vs no supervisado vs sermisueprvisado.
Bathc vs onlinea leaning.
l modelo se entra en lotes o se actualiza 


###    **CHUNK:Feature vectors**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
SON UNA FORMA DE AGARRAR RASGOS Y ASPECTOS DE UN OBJETO Y PONERLO DE MANERA NUMERICA para que puedan funcionar.

Se utilizan para representar características simbólicas o numéricas llamadas features.
Permiten analizar un objeto desde una perspectiva matema´tica
Los algoritmos de machone learning tipicamente requieren respentaciones numericas para poder ejecutar el cómputo.
Uno de los feature vectors mas conocido el el RGB,

Determino muchas veces que valores se incorporarn y cuales se dejan afuera.

Pensar el probelma muy bien y determinar lo que importa de lo que no importa.


Procesamiento de imágnees:
Gradicentes, bordes, áreas, colores.

Reconocimiento de voz
Disntacia de sonidos, nivel de ruido, razon ruido, señal. Teoria de la Información

Spam, Direccion ip, estructura del texto, frecuencia de palabras, encabezados.
ÑLo importante es obtener vectores relevantes.

//Un estudiante propuso un ejemplo de dendrolgoía.

###    **CHUNK:Métricas de distancia**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

Metricas de distancia nos permiten cuantificar que lejos o cerca están los vectores a nuestro algoritmo.

Optimización. Buscan optimizar la distancia entre vectores.
lOS ALGORIMTOS DE OPTMIZACIÓN MUCHAS VECES BUSCAN saber la distancia entre features.

Distancia Manhattan

|a-c| +|b-d|
Da un vectir de distancia.
Primero se representan la ifno en vectores luego se miden.

¿Que otros metodos d emedir distancia?








###    **CHUNK:Introducción al agrupamiento**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
clustering, algoritmos de clustering.
Es una forma de calsificar, nos permite entender estructura interna d elos datos cuando no es necesario usar etiwteas
Obtenemos info valiosa al clasificar los grupos que viven en los datos.

no supervisado

motores de busqueda, el platziMasrer selection algoritm.
Medicina para saber si tenemos riesgo o no según unas variabels de sufrir una enfermedad.
En genética.

¿Como puedo hace run algoritmo de clustering que recib una secuencia genética maliciosa y me devuelva si la persona está contagiada o no.
Esto dependería de si se ha secuenciado la enfermedad o no.
https://towardsdatascience.com/the-5-clustering-algorithms-data-scientists-need-to-know-a36d136ef68

https://media.springernature.com/original/springer-static/image/chp%3A10.1007%2F978-981-13-7403-6_9/MediaObjects/469174_1_En_9_Fig1_HTML.png


###    **CHUNK:Agrupamiento jerárquico-algoritmo**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
Toma los puntos mas cercanos los ponen un cluster, y luego compara distancia entre cluster y punto ma´s cercano.
Cada datapoitn es un cluster individual.
Dendrograma señala las relaciones entre individuos y grupo.

El algoritmo comienza tratando cada objeto como un cluter individual y luego realiza los siguientes pasos de manera ecursiva:
    * identifica los dos clusters con menor distancia ( lso más imilares)
    * Agrupa los dos cluster en uno nuevo.
 El put fina es un dendrograma que muestra la relación entre objetos y grupos.
 Es importante determianr que medda de distancia vamos a utilizar y los puntos a tuilziar en cada cluster. (Linkage criteria)
 
 Metodo para medir distancia, single linkage
 
Tomar los mas lejanos complete linkage
buscar lso grupos promedio avergae linkae.


 ¿Puede ser un tema del conocimiento un dendrograma?
 Es decir, tengo temas dispersos que agrupo en un cluster hasta n...
 
 Hayy que escribir un progama qu eme permita hace rle clustering de terminos.
 
 * Un array de numeros cualquiera
 * que me determine la distancia entre dos puntos mas cercados y me agrupe esos valores en un conjunto.
 * Luego debo decirle que me tomeeste conjunto (como lo represento en un número?) y luego lo comparo con uno que me permtia a otro punto.
    Esto N veces. Luego hasta el valro más lejano y luego al romedio.
    
https://scikit-learn.org/stable/modules/clustering.html     
 

###    **CHUNK:Agrupamiento K-means**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
Genera clusterings.
Asina putnas al azar y dice cuantos grupos va analizar, si k es igual a n existen n. Luego genramso las distancias entre todso los puntos
(o feature vectores) Genemaros la media, mredia iterativa.
Y lo asignamos en el centroide, o la media del grupo. Y luego volvemos a mdeir las disntancia entre ellos hasat que ya no hayna mejoras o el algoritmo
 hizo convergencia
 
Es un algoritmo que agrupa utilizando centroides.
El algoritmo funciona asignando puntos al azar. K define clusters
    + En cada iteración el punto se ajusta a su nuevo centroide y cada punto recalcula con la distnaci con respecto a los centroides.
    + lo spuntos se reasignan al nuevo centro
    + El algortimo se Repite de manera iterativa hasta que  ya no existen mejoras.

Escoher un k correcto de tamaño n.
Un conocimiento del domiio del problema me da las intuiciones para lelgar a un agrupameinto relevante.

Como implemento un kMeans?    

La tecnica de Feynman de la que habla es una tecnica de aprendizaje:
 En la que tu intentas lograr por tus medios el codigo que haga una cosa en especifico, 
 en este caso tenias que hacer el codigo de k means, y despues de fracasar xd ver como lo hicieron en las librerias 
 que son codigo que hizo gente que le dedico tiempo a pensar como desarrollarlo.
     
 
###    **CHUNK:Otras técnicas de agrupamiento**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html


tECNICAS DE AGRUPAMIENTO CONSISTE EN DIVIDIR A UNA POBLACIÓN EN GRUPOS CON LAS CONSECUENCIA DE QUE LOS FATOS EN UN GRUPO SON MÁS IMILARES ENTRE ELLOS
QUE ENTRE LOS OTROS GRUPOS.

Agrupamiento esticto: Hard clusteringEn el cual cada dato pertenece a un grupo u otro, No hay puntos medios.
Agrupameinto Laxo: Sfot CLusterins.en el cual en lugar de asignar un dato a un grupo, se asigna probabilidades a cada dato de pertenecer o no a un grupo

Un punto muy importante que debes considerar cuando ejecutas técnicas de agrupamiento es que debes definir muy claro a qué te refieres cuando hablas de similitud entre puntos, porque esto puede ayudarte a definir el algoritmo correcto para tus necesidades particulares.
​
A grandes rasgos existen cuatro aproximaciones para definir similitud:
​

Modelos conectivos: Estos modelos asumen que los puntos más similares son los que se encuentran más cercanos en el espacio de búsqueda. Recuerda que este espacio puede ser altamente dimensional cuando tus feature vectors definen muchas características a analizar.
 Una desventaja de este tipo de modelos es que no escalan para conjuntos de datos grandes (aunque es posible utilizar una muestra y aplicar técnicas de estadística inferencial para obtener resultados).

Modelos de centroide: Este tipo de modelos definen similitud en términos de cercanía con el centroide del grupo. Los datos se agrupan al determinar cuál es el centroide más cercano.

Modelos de distribución: Este tipo de modelos trata de asignar probabilidades a cada dato para determinar si pertenecen a una distribución específica o no (por
ejemplo, normal, binomial, Poisson, etc.).

Modelos de densidad: Estos modelos analizan la densidad de los datos en diferentes regiones y dividen el conjunto en grupos. Luego asignan los puntos de acuerdo a las áreas de densidad en las que se haya dividido el dataset.
​
Acuérdate que no tienes que casarte con un modelo específico. Muchos de los mejores Ingenieros de Machine Learning y Científicos de Datos utilizan varios modelos con el mismo conjunto de datos para analizar el rendimiento de los diversos algoritmos que tienen a su disposición. Así que experimenta y siempre compara tus resultados antes de tomar una decisión.

E agrupameinto no es supervisado, poque no tenemos etiquetas.


###    **CHUNK:Introducción a la clasificación**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
Requiere etiquetas, artimos del supuesto de que teneos información importan.

ImageNet
Mnist

Es el proceso mediante el caul se predice la clase de cierto dato.
Es n aprendizaje supervisado ya que para que funcione se necestan etiquetas con los datos.
Se utilzia en muchos dominios, incluyendo la medicina, aprobación crediticia, reconocimiento de imágenes, vehículos autónomos, entre otros.
Sigue dos pasos.Aprendizaje, creación y clasificación.

Diferencias entre aprendizaje Supervisado y no supervisado.

* Encontramos cluster en el no supervisado data set, mestreado, y el supervisado clasificamos según un parámetro.


###    **CHUNK:Clasificación K-nearest neighbors**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

Pardte de supuesto de una clasificación previa y queremos encontrar la clase de un vector, datapoitn, qu eno sabemso clasificarlo.
K neibors es los vecinos que nos permiten clasificar el data point.

* Trata de encontrar los vecinos cercanos.
* K se refiere a la cantidad de vecinos que se utilziará para clasiicar un ejemplo que aun no ha sido clasificado.
    * Si un k es par no podría decidir cuando es una distancia.
* Sencillo implemntar.
* A que tipo de ceclulas nos estamos confrontando, usamos el knearest neibogr, a qué cula se paece?
* mUY COSTOS no sirve con datos de alta dimensionalidad:


1. Construir un feature Vectors.


###    **CHUNK:Técnicas de clasificación**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

Clasificadores lineales
​
Estos tipos de clasificadores se distinguen porque dividen el conjunto de datos 
con una línea (que puede ser multidimensional dependiendo de 
la cantidad de features que hemos utilizado para definir a nuestros datos).
Esto genera áreas dentro de nuestro espacio de búsqueda 
para que cuando coloquemos un nuevo dato podamos clasificarlo fácilmente.
​
El problema con este tipo de modelos es que son pocos flexibles cuando el 
conjunto de datos no puede ser separado fácilmente con una simple línea; por 
ejemplo, cuando necesitáramos una figura más compleja para dividirlo (como un polígono).


Nearest neighbor
​
Los modelos que utilizan nearest neighbor se apoyan 
de los datos que ya han sido clasificados para determinar 
la distancia entre sus “vecinos más cercanos.
” El algoritmo más común que utiliza esta técnica se llama K-nearest neighbors 
y la K representa el número de vecinos que se utilizarán para clasificar los datos.
 En pocas palabras, se identifican los datos más cercanos y en el caso más sencillo
  se hace una votación simple (por ejemplo, 5 azules, 2 rojos, por lo tanto azul).
​
Una característica de estos modelos es que “dibujan” 
una línea que se asemeja a una costa para clasificar los datos. 
Mientras K sea más grande la “línea costera” se alisa y se
 asemeja más y más a una línea simple. Por lo tanto, 
 la definición de K tiene un impacto importante en el 
 desempeño de nuestro algoritmo de clasificación.
​

Support Vector Machines
​
Estos algoritmos se diferencian por tener la habilidad 
de generar figuras complejas (polígonos) que pueden agrupar datos. 
Si la figura que tendríamos que dibujar para dividir nuestros datos es diferente a una línea
 (círculos, polígonos, etc.), entonces estos modelos son una buena opción.
​

Árboles de decisión
​
Este tipo de algoritmos nos permiten generar una árbol que tenemos que recorrer 
y tomar decisiones cada vez que avanzamos en un nivel. Por ejemplo:
​

Si un feature en análisis es mayor a 5, dibuja la línea y=2x+3, de lo contrario dibuja y=-3x+5
Si el feature siguiente es menor a 2, dibuja otra línea y así sucesivamente.
​
Conclusiones
​
Recuerda que la decisión de qué algoritmo utilizar depende de la forma en la que tengas 
tus datos y la precisión que desees obtener (a cambio de excluir o incluir falsos positivos y negativos).
 Otro punto a considerar es que estos algoritmos deben ser entrenados con datos previos y la calidad de
  estos datos y del modelo subsecuente importan mucho para obtener la mejor clasificación.
​
Te invito a que consultes la documentación de Scikit-learn para que puedas profundizar 
en la forma en que funcionan estos algoritmos (y muchos otros) y puedas saber qué tipo de
parámetros se pueden ajustar y cuál es la forma de los datos que esperan.
Aquí está el vínculo a la documentación:
 
 https://scikit-learn.org/stable/user_guide.html
  



###    **CHUNK:Cum Hoc Ergo Propter Hoc**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


###    **CHUNK:Cum Hoc Ergo Propter Hoc**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■




###    **CHUNK:Cum Hoc Ergo Propter Hoc**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■







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
## GLUE: EXÁMEN:
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

Dado que se obtuvo una muestra de los alumnos de Platzi, ¿se pueden realizar conclusiones sobre toda la población de estudiantes en línea?

E

La clasificación pertenece a la siguiente categoría de Machine Learning
a

Una gráfica se puede leer aún si no existen etiquetas
d

La matemática puede convertir datos malos en resultados buenos
a

¿Cuál fue el programa que le ganó en 1997 a Kaspárov en Ajedrez?
b

Cuál de las siguientes no es una aplicación del Teorema de Bayes?
a

Uno corre el riesgo de caer en la Falacia del Francotirador de Texas cuando realiza experimentos sin una hipótesis
b

El Teorema de Bayes nos permite
b

¿Cuál no es un algoritmo de clasificación?
a

La regresión logística modela la probabilidad de que un tipo de evento suceda
https://es.wikipedia.org/wiki/Regresi%C3%B3n_log%C3%ADstica
b

¿Qué es mejor, un aumento del 10% o del 30%?
c

El algoritmo de agrupamiento jerárquico termina una vez que existen cuántos grupos
b


El agrupamiento K-means pertenece a la siguiente categoría de Machine Learning
b

Siempre que existe un evento extremo el siguiente evento tenderá a regresar a la media
d


¿Qué parámetro controla K dentro del algoritmo de K-nearest neighbors?
b


La correlación y la causalidad es lo mismo
a


¿Para qué nos sirven las métricas de distancia en Machine Learning?
e

El centroide, dentro del agrupamiento de K-means, es estático
c


¿Cuál no es un algoritmo de agrupamiento?
c

Antes de que se realice un examen médico, ¿cuál es tu probabilidad (sin mayor información) de padecer una enfermedad?
d

Cómo se lee la siguiente expresión: P(H | E)
e

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
