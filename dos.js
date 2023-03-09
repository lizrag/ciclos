// --2)Realice el mismo metodo anterior para generar 
// una CLABE interbancaria, pero para generar 
// los numeros aleatorios utilice los metodos random correspondientes,
// a este metodo nombrelo generaCLABE2()

function generarClabe2(){
    let clabe = "";
    for (let i=0; i<=18; i++){
        numeros = Math.floor(Math.random()*57)+48;
        numeros_random = String.fromCharCode(numeros);
        clabe= clabe+numeros_random;
    }
    return clabe;
}

console.log(generarClabe2()); 