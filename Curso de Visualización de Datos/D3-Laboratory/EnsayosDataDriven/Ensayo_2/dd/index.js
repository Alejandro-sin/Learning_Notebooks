import {select, csv} from 'd3.js';

const svg = select ('svg');
const width = +svg.attr('width');
const height =+svg.attr('height');

csv('data.csv').then(data =>{
    console.log(data)
});

