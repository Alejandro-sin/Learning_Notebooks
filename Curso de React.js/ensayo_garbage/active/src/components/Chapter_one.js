import React from   'react';
import atonm from '../images/atonm.png';
import "../styles/style.css";


/* Defino la clase Badge */

class Chapter_one extends React.Component{
/* 1. Todos los componentes necesitan al menos un método, que es el método render, render
define cual es el resultado que vemos en pantalla. Render retorna */
    render(){
        return <div class ="Chapter">
                <div class= "wall">
                    <h1>
                        Aprendiendo <br></br>React
                    </h1>
                    
                    <div class="wall-logo">
                        <img src={atonm} alt="post react" width="700"/>
                    </div>
                    
                    <div>
                    <p> 
                        Este capítulo consistira en mostrar los usos de la librería-framework React
                        de forma tal sea una una guía dinámica del desarrollo.    
                        Usaremos propt para asociar elementos a propiedades de etiquetas
                        React al renderizar las imagenes les añade en el atributo src una direcció y un .hash con el fin de almacernar
                        en el caché las imagenes precargadas. "/static/media/atonm.cea1e95d.png"
                    </p>
                    </div>
                </div>

            <div class="footer">
                <h4> Pie página </h4>
                <p> @aprendiendoreact</p>
            </div>
        </div>;
    }

}


 export default Chapter_one;