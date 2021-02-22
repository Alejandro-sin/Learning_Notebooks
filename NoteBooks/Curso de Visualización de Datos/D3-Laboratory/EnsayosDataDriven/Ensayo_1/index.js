var datos = [12,14,100,101,122,24,25,37,57,155,33];

const x = d3.scaleLinear()
    .domain([0,d3.max(datos)])
    .range([0,300])


function pintar(){
    d3.selectAll("p").on("click", function(){
    d3.select(this).style("color", "red")})
};

function graficar(){
    d3.select(".barras")
        .selectAll("div") 
        .data(datos)
        .enter()
        .append('div')
        .style("width", function(d){
            return x(d)+'px';
        })
        .text(function(d){
            return d;
        })
}


function seleccionar(){
    d3.selectAll('div')
        .style('background-color','green')
};




function barChart(){
 /*    d3.select('.bloque')
    //Para seleccionar tood lo que hay adentro
    .selectAll('div')
        .style('background-color','red') */

d3.select('.histograma')
    .selectAll('div')
    .data(datos)
    .enter()
    .append('div')
    /* .style('height', function(d){
        return d +"px";
    }) */
    .style('width', function(d){
        return x(d) +"px";
    })
    .style('background-color', function(d){
        if (d > 100){
            return 'red';
        }if(d < 50){
            return 'blue';
        }
    })
    .text(function(d){
        return d
    });
};


function sqrChart(){

    d3.select('.cuadrados')
        .selectAll('div')
        .data(datos)
        .enter()
        .append('div')
        .text(function(d){
            return d
        })
        .style('width', function(d){
            return x(d) + "px"
        })
        .style('height', function(d){
            return x(d) + "px"
        })

}

function histogramaH(){
    d3.select(".histogramaH")
        .selectAll('div')
        .data(datos)
        .enter()
        .append('div')
        .style("height", function(d){
            return x(d) + "px"
        })

}



function circulosSVG(){
    const SortData =  datos.sort((a,b)=>a-b)
    const svg = d3.select('body')
        .append('svg')
        .attr('class', 'svgContainer_circles')
    const c = svg.selectAll('circle')
        .data(SortData)
        .enter().append('circle')
    c.attr("cx",function(d,i){
            return( i *80 )+25;
        })
        .attr("cy", 500/2)
        .attr("r" , function(d){
            return  d
        })
        .attr('class', 'circulosSVG')
}


function barrasSVG(){

    let w = 500
    let h = 500
    var svg = d3.select('body')
        .append('svg')
        .attr("width", w)
        .attr("height", h);

    svg.selectAll('rect')
        .data(datos)
        .enter().append('rect')
        .attr('class','rectSVG')
        .attr("width", 10)
        .attr("height", 10)      
        .attr("x", function(d,i){
            return i*20 + 30;
        })
        .attr("height", function(d){
        return d;
        })
        .attr("y", function(d){
            return h-d;
        })
    svg.selectAll("text")
        .data(datos)
        .enter()
        .append("text")
        .text(function(d){
            return d;
        })
        .attr("x", function(d,i){
            return i*21+ 40;
        })
        .attr("y", function(d){
            return h -d -3;
        })
}