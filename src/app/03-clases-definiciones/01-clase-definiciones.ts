/*
*    Objetivo:
*        Ver rápidamente las definiciones de la clase
?    Tips:
?        Ctrl + P    luego escribir la @
?        Ctrl + Shift + o    luego escribir la @
?        Se pueden agrupar si después de la @, se escriben :
*/


class SuperHeroe {

    nombre: string;
    poder: string;
    edad: number;
    pasatiempo: string;

    private _nombreSecreto: string;

    constructor() { }

    usarPoder() {}

    volar() {}

    correr() {}

    caminar() {}

    revivir() {}

    nombre2: string;
    poder2: string;
    edad2: number;
    pasatiempo3: string;

    set nombreSecreto(nombre) {
        this._nombreSecreto = nombre;
    }

    get nombreSecreto() {
        return this._nombreSecreto;
    }
}
