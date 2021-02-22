const svg = d3.select('svg');
//El más se usa para parsear
const h = +svg.attr('height')
const w = +svg.attr('width')


const circle = svg.append('circle')
    .attr('r', 100)
    .attr('cx', w/4)
    .attr('cy', w/4)
    .attr('stroke','red');


const circle_L = svg.append('circle')
    .attr('r', 10)
    .attr('cx', w/4 -50)
    .attr('cy', w/4)
    .attr('stroke','red')
    .attr('fill', 'white');


const circle_D = svg.append('circle')
    .attr('r', 10)
    .attr('cx', w/4 + 50)
    .attr('cy', w/4)
    .attr('stroke','red')
    .attr('fill', 'white');


const rect = svg.append('rect')
    .attr('x', 100)




// COmo funcionan las asincornas SetTimeoUt aqui.lines