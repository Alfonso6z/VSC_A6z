/*
*    Objetivo:
*       Cambiar únicamente la refencia de SuperHeroe a Heroe
&       No reemplazar los strings
?    Tips:
?        Replace Symbol
?        F2
*/
import { SuperHeroe } from './extra/classes';


const wolverine = new SuperHeroe();
const ironman   = new SuperHeroe();
const spiderman = new SuperHeroe();

function saludar() {
    return 'El SuperHeroe Wolverine es genial!';
}

function gritar() {
    return 'El SuperHeroe en este string no se debe de cambiar';
}

