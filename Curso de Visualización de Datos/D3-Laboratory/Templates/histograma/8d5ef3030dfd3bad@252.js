// https://observablehq.com/@d3/histogram@252
export default function define(runtime, observer) {
  const main = runtime.module();
  const fileAttachments = new Map([["unemployment-x.csv",new URL("./files/dataTransform",import.meta.url)]]);
  main.builtin("FileAttachment", runtime.fileAttachments(name => fileAttachments.get(name)));
  main.variable(observer()).define(["md"], function(md){return(
md`# Histogram

Unemployment rate by county, August 2016. Source: [Bureau of Labor Statistics](http://www.bls.gov/lau/#tables).`
)});
  main.variable(observer("chart")).define("chart", ["d3","width","height","bins","x","y","xAxis","yAxis"], function(d3,width,height,bins,x,y,xAxis,yAxis)
{
  const svg = d3.create("svg")
      .attr("viewBox", [0, 0, width, height]);
  
  svg.append("g")
      .attr("fill", "steelblue")
    .selectAll("rect")
    .data(bins)
    .join("rect")
      .attr("x", d => x(d.x0) + 1)
      .attr("width", d => Math.max(0, x(d.x1) - x(d.x0) - 1))
      .attr("y", d => y(d.length))
      .attr("height", d => y(0) - y(d.length));

  svg.append("g")
      .call(xAxis);
  
  svg.append("g")
      .call(yAxis);
  
  return svg.node();
}
);
  main.variable(observer("data")).define("data", ["d3","FileAttachment"], async function(d3,FileAttachment){return(
Object.assign(d3.csvParse(await FileAttachment("unemployment-x.csv").text(), ({rate}) => +rate), {x: "Unemployment (%)", y: "Counties"})
)});
  main.variable(observer("bins")).define("bins", ["d3","x","data"], function(d3,x,data){return(
d3.histogram()
    .domain(x.domain())
    .thresholds(x.ticks(40))
  (data)
)});
  main.variable(observer("x")).define("x", ["d3","data","margin","width"], function(d3,data,margin,width){return(
d3.scaleLinear()
    .domain(d3.extent(data)).nice()
    .range([margin.left, width - margin.right])
)});
  main.variable(observer("y")).define("y", ["d3","bins","height","margin"], function(d3,bins,height,margin){return(
d3.scaleLinear()
    .domain([0, d3.max(bins, d => d.length)]).nice()
    .range([height - margin.bottom, margin.top])
)});
  main.variable(observer("xAxis")).define("xAxis", ["height","margin","d3","x","width","data"], function(height,margin,d3,x,width,data){return(
g => g
    .attr("transform", `translate(0,${height - margin.bottom})`)
    .call(d3.axisBottom(x).ticks(width / 80 ).tickSizeOuter(0))
    .call(g => g.append("text")
        .attr("x", width - margin.right)
        .attr("y", -4)
        .attr("fill", "currentColor")
        .attr("font-weight", "bold")
        .attr("text-anchor", "end")
        .text(data.x))
)});
  main.variable(observer("yAxis")).define("yAxis", ["margin","d3","y","height","data"], function(margin,d3,y,height,data){return(
g => g
    .attr("transform", `translate(${margin.left},0)`)
    .call(d3.axisLeft(y).ticks(height / 40))
    .call(g => g.select(".domain").remove())
    .call(g => g.select(".tick:last-of-type text").clone()
        .attr("x", 4)
        .attr("text-anchor", "start")
        .attr("font-weight", "bold")
        .text(data.y))
)});
  main.variable(observer("height")).define("height", function(){return(
500
)});
  main.variable(observer("margin")).define("margin", function(){return(
{top: 20, right: 20, bottom: 30, left: 40}
)});
  main.variable(observer("d3")).define("d3", ["require"], function(require){return(
require("d3@5")
)});
  return main;
}
