//Aqui pongo todas las trnasformaciones con el arreglo de datos de prueba.

//Aqui pongo todas las trnasformaciones con el arreglo de datos de prueba.

// DATA PRACTCA
// Hace parte del primer gráfico para ver la totalidad de con interaciones.
const dataSet =[{"name":"Davy","interWS":702,"interGM":149,"interactions":851},
{"name":"Egan","interWS":500,"interGM":891,"interactions":1391},
{"name":"Shannan","interWS":557,"interGM":849,"interactions":1406},
{"name":"Nester","interWS":869,"interGM":491,"interactions":1360},
{"name":"Mab","interWS":378,"interGM":816,"interactions":1194},
{"name":"Merv","interWS":497,"interGM":948,"interactions":1445},
{"name":"Marthena","interWS":642,"interGM":936,"interactions":1578},
{"name":"Trudy","interWS":33,"interGM":210,"interactions":243},
{"name":"Christine","interWS":133,"interGM":872,"interactions":1005},
{"name":"Mikel","interWS":402,"interGM":32,"interactions":434},
{"name":"Rebeka","interWS":411,"interGM":541,"interactions":952},
{"name":"Willette","interWS":788,"interGM":591,"interactions":1379},
{"name":"Laird","interWS":339,"interGM":327,"interactions":666},
{"name":"Freddi","interWS":276,"interGM":448,"interactions":724},
{"name":"Corbie","interWS":296,"interGM":443,"interactions":739},
{"name":"James","interWS":105,"interGM":22,"interactions":127},
{"name":"Ilario","interWS":383,"interGM":70,"interactions":453},
{"name":"Muffin","interWS":847,"interGM":684,"interactions":1531},
{"name":"Clevey","interWS":108,"interGM":390,"interactions":498},
{"name":"Melosa","interWS":203,"interGM":478,"interactions":681},
{"name":"Arlan","interWS":866,"interGM":380,"interactions":1246},
{"name":"Elladine","interWS":561,"interGM":12,"interactions":573},
{"name":"Prescott","interWS":565,"interGM":610,"interactions":1175},
{"name":"Court","interWS":94,"interGM":688,"interactions":782},
{"name":"Lyndel","interWS":26,"interGM":724,"interactions":750},
{"name":"Xena","interWS":107,"interGM":53,"interactions":160},
{"name":"Woody","interWS":546,"interGM":165,"interactions":711},
{"name":"Leone","interWS":244,"interGM":427,"interactions":671},
{"name":"Charlena","interWS":447,"interGM":685,"interactions":1132},
{"name":"Janis","interWS":121,"interGM":884,"interactions":1005},
{"name":"Lorri","interWS":936,"interGM":652,"interactions":1588},
{"name":"Kirsteni","interWS":959,"interGM":26,"interactions":985},
{"name":"Aeriell","interWS":107,"interGM":320,"interactions":427},
{"name":"Stafford","interWS":326,"interGM":357,"interactions":683},
{"name":"Galven","interWS":238,"interGM":740,"interactions":978},
{"name":"Lamar","interWS":563,"interGM":408,"interactions":971},
{"name":"Meghan","interWS":718,"interGM":490,"interactions":1208},
{"name":"Dalia","interWS":984,"interGM":479,"interactions":1463},
{"name":"Marya","interWS":694,"interGM":747,"interactions":1441},
{"name":"Ruttger","interWS":557,"interGM":429,"interactions":986},
{"name":"Tania","interWS":361,"interGM":797,"interactions":1158},
{"name":"Hildegarde","interWS":616,"interGM":44,"interactions":660},
{"name":"Peggy","interWS":614,"interGM":749,"interactions":1363},
{"name":"Boone","interWS":782,"interGM":992,"interactions":1774},
{"name":"Mirabelle","interWS":343,"interGM":773,"interactions":1116},
{"name":"Dougie","interWS":609,"interGM":713,"interactions":1322},
{"name":"Katy","interWS":774,"interGM":714,"interactions":1488},
{"name":"Shay","interWS":172,"interGM":506,"interactions":678},
{"name":"Faunie","interWS":370,"interGM":281,"interactions":651},
{"name":"Elwira","interWS":94,"interGM":745,"interactions":839},
{"name":"Batholomew","interWS":568,"interGM":426,"interactions":994},
{"name":"Cherlyn","interWS":764,"interGM":330,"interactions":1094},
{"name":"Sayers","interWS":853,"interGM":404,"interactions":1257},
{"name":"Othilie","interWS":165,"interGM":21,"interactions":186},
{"name":"Goldi","interWS":750,"interGM":608,"interactions":1358},
{"name":"Wilt","interWS":551,"interGM":47,"interactions":598},
{"name":"Jacinta","interWS":934,"interGM":602,"interactions":1536},
{"name":"Abeu","interWS":585,"interGM":24,"interactions":609},
{"name":"Matias","interWS":768,"interGM":203,"interactions":971},
{"name":"Ky","interWS":200,"interGM":549,"interactions":749},
{"name":"Zorana","interWS":593,"interGM":17,"interactions":610},
{"name":"Kenna","interWS":753,"interGM":303,"interactions":1056},
{"name":"Annie","interWS":516,"interGM":29,"interactions":545},
{"name":"Christean","interWS":91,"interGM":458,"interactions":549},
{"name":"Tam","interWS":192,"interGM":197,"interactions":389},
{"name":"Marybeth","interWS":396,"interGM":220,"interactions":616},
{"name":"Cynthy","interWS":24,"interGM":823,"interactions":847},
{"name":"Egan","interWS":334,"interGM":779,"interactions":1113},
{"name":"Rae","interWS":136,"interGM":198,"interactions":334},
{"name":"Pia","interWS":454,"interGM":445,"interactions":899},
{"name":"Kaitlin","interWS":890,"interGM":633,"interactions":1523},
{"name":"Shep","interWS":98,"interGM":195,"interactions":293},
{"name":"Zitella","interWS":969,"interGM":853,"interactions":1822},
{"name":"Mathias","interWS":193,"interGM":538,"interactions":731}]

//Máximo de interacciones
const maxInteractions = d3.max(dataSet,function(d){
    return d.interactions;
    console.log(maxInteractions)
})


//Mínimo de interacciones

const minInteractions = d3.min(dataSet, function(d){
    return d.interactions;
})



//■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■HOST EN GENERAL■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
// MAP ------------------------------------------------------------------------------------------------------------------------------------//
//Con esto tengo el arreglo de solo los datos de las interaciones totales.

const hostInteractions = dataSet.map(function(d,i){
    return{
        name: d.name,
        index: i+1,
        interactions: d.interactions
    }
})

console.log(hostInteractions)


//FILTER------------------------------------------------------------------------------------------------------------------------------------//
//Quiero tener 3 rangos los mayores a 1500, los mayores a 700, los mayores a 300. Interacciones.

//Mayores a 1500

const highInteractions =  hostInteractions.filter(function(d){
    return d.interactions >1500;
})

console.log(JSON.stringify(highInteractions));

//Mayores a 700

const mediumInteractions =  hostInteractions.filter(function(d){
    return d.interactions >700;
})

console.log(JSON.stringify(mediumInteractions));


//Menores a 700
const lowInteractions =  hostInteractions.filter(function(d){
    return d.interactions <700;
})

console.log(JSON.stringify(lowInteractions));


//SORT------------------------------------------------------------------------------------------------------------------------------------//
//Los tengo de mayor a menor. Y obtengo los primeros 5.
const dataSort = dataSet.sort(function(a,b){
    return b.interactions -a.interactions;
}).slice(0,5)
console.log("DataSort")
console.log(JSON.stringify(dataSort));


//■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ HOST GENERAL ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

// HAGO UN SORT  del sort

const interactionSort = dataSort.map(function(d){
    return {interactions: d.interactions}
})
const nameSort=dataSort.map(function(d){
    return {name: d.name}

})
console.log(nameSort)
console.log(interactionSort)






/* 
const hostInteractions = dataSet.map(function(d,i){
    return{
        name: d.name,
        index: i+1,
        interactions: d.interactions
    }
})

console.log(hostInteractions)

 */