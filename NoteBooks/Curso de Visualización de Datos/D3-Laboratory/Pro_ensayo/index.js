

/* 
var svg = d3.select('#vis')
    .append("svg");

    svg.append('rect')
    .attr('class',"rectTest")
    .attr('x',100 )
    .attr('y',50)
    .attr('width', 200)
    .attr('height',100 )
 
}; */
var svg =d3.select('#another')
    .append("svg")
    svg.attr('width', setTimeout(function(){
        return 100;
        
    },300));
        .attr('class', "svg_3" )
        


