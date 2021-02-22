const comida ="Papas"

function estrcutura_switch(comida) {
    switch (comida){
        case "Arepaita":
            console.log(comida)
            break;
        case "Arepota":
            console.log(comida)
            break;
        case "Arepato":
            console.log(comida + " rico")
            break;
        default:
            console.log("Comida areposa")
    }
}

estrcutura_switch("Arepato")