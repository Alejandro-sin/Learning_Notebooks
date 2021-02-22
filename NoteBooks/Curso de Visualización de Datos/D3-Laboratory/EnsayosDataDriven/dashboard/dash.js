
var dataM=[1,2,50,50,5,6,7,8,9,10,11,15,450,25,50,100,0,5,6,200,20,25,50,100,120,200,7,8,10,200,20,25,50,100,120,200,150, 100,50]

var dataLoad = []

function dataload(){
    d3.json("dataSets/data.json").then(function(data){
        dataLoad = data
        console.log(dataLoad)
        barchart()
    })
}


function piechart(){
}

//Para la vista generals de los host
//La idea es que la grafica se organice

function barchart(){
    let w = 500
    let h = 300
    var svg = d3.select('div')
        .append('svg')
        .attr("width", w)
        .attr("height", h);
    svg.selectAll('rect')
        .data(dataM)
        .enter().append('rect')
        .attr('class','rect_svg')
        .attr("width", 10)
        .attr("height", 500)
        .attr("x", function(d,i){
            return i*10 + 15;
        })
        .attr("height", function(d){
        return d;
        })
        .attr("y", function(d){
            return h - d;
        })
}




