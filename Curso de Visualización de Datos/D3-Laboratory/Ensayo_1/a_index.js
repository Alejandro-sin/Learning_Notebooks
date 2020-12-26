
/* // Selecionar elementos de DOM.
d3.select()
d3.selectAll()


// Puedo usar  los selecotres así para darle color

d3.select('h2').style('color','blue')
    .attr('class','heading')
    .text('Alejandro',) // Estoy cambiando el conentido de una etiqueta.

// Puedo hacer  que se me inserten nuevas etiquetas

d3.select('body').append('p').text('Aqui va un texto')
d3.select('body').append('p').text('Aqui va un texto')
d3.select('body').append('p').text('Aqui va un último texto')
d3.select('body').append('ol').text('Aqui va una lsita ordenada')
d3.select('body').append('div').text('Est es un div')
d3.select('body').append('h1').text('Aqui va un titulo')

// Puedo tambien hacer  un cambio de multples etiquetas

d3.selectAll('p').style('color', 'blue')

 */
/* //Cargado de datos
 
let dataSet = [1,2,3,4,5];

d3.select('body')
    .selectAll('p') //Estos no existen aun
    .data(dataSet) // Esto pasa nuestro data set como argumento.
    .enter() //
    .append('p')
    .text(function(d){return d; }) // Le pasamos esta función y nos dalara los valores de data.
 */

//Creando un Bar Char

// Vaos a usar el SVG para crear un gráfico de barras


/* var dataset = [1,2,3,4,5,6,7]
var svgWidth = 400, svgHeight = 100, barPadding = 5; // Defino las variables del tamaño del contenedor. Y la separación entre las barras
var barWidth = (svgWidth/ dataset.length); // Defindo el ancho de las colimnas dividiendo el ancho total del SVG sobre 
// El tamaño del data set enelementos.


// Este framgento de código estoy  asignandole a una variable svg una seleción de la etiqueta svg.
var svg = d3.select('svg')
//Luego con .attr estoy uniendo las dimensiones que estableci inicialmente con los atributos de ancho y alto de la etiqueta
//en si
    .attr("width",svgWidth )
    .attr("Height",svgHeight )
 */

 
/* //CREANDO ESCALAS    
var yScale = d3.scaleLinear()
//Esto me devuelve el máximo valor del data set.
    .domain([0,d3.max(dataset)])
    .range([0, svgWidth]);

var xScale =  d3.scaleLinear()
    .domain([0,d3.max(dataset)])
    .range([svgHeight, 0 ]);

var x_axis = d3.axisBottom().scale(xScale);
var y_axis = d3.axisLeft().scale(yScale);

svg.append("g")
    .attr("transform", "translate(50,10")
    .call(y_axis);

var xAxisTranslate = svgHeight - 20;

svg.append("g")

svg.append("g")
    .attr("transform", "translate(" + xAxisTranslate+")")
    .call(x_axis); */

//CREANDO BARCHAR
// Estoy usando rectangulos, seleciono todos los rectangulos.
/* var barChart =  svg.selectAll("rect") // Al no haber ninguno es una selccion vacía
    .data(dataset) // Esto me trae mi data set y me se queda en un estado de esera.
    .enter()  // Esto em trae  el data set del estado de quietud  para posteriores operaciones, en CADA item del data set.
    //OPEREACIONES AL DATA SET:
    // lo que estoy viendo son lso atributos del rectangulo.
    .append("rect") // Adjunto rectangulos.
    // la función d me toma los datos de mi data set , estoy diciendo, que tome el atributo y, de cada rectangulo.
    // y que me devuelva un valor que será una diferencia entre la altura de mi SVG y mi dato de mi data set( rectangulo))
    .attr("y", function(d){
        return svgHeight - d
    })
    //Aqui le estoy diciendo que mi altura es igual al valor que tengo en mi data set.
    .attr("height", function(d){
        return d;
    })
    // Aqui le estoy diciendo que el ancho de mi rectngulo será la diferenica entre el ancho de mis olumnas menso el paddign que las sepra
    .attr("width", barWidth - barPadding)

    //Aqui trnaformo.
    .attr("transform", function (d,i){
        var translate = [barWidth * i, 0];
        return "translate("+ translate +")";
    })

    //CREANDO ETIQUETAS.

var  text  = svg.selectAll("text")
    .data(dataset)
    .enter()
    .append("text")
    .text(function(d){
        return d;
    })
    // Queremos que el texto sean un poco mas alto, por lo que resatmos 2 pixeles mas de el alto.
    .attr("y", function(d,i){
        return svgHeight -d -2;
    })
    //Este es el punto  donde empieza cada rectangulo., lo obtengo usando los valores del ancho de la barra y el indice de
    //cada elemento de la data.
    .attr("x", function(d,i){
        return barWidth * i;
    })
    .attr("fill", black)
 */

