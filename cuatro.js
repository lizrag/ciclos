// --4)Realice el mismo metodo anterior para generar 
// un numero de cuenta bancaria, pero para generar 
// los numeros aleatorios utilice los metodos random correspondientes,
// a este metodo nombrelo generaCuentaBancaria()

function generarCuentaBancaria(){
    let clabe = "";
    for (let i=0; i<=14; i++){
        numeros = Math.floor(Math.random()*57)+48;
        numeros_random = String.fromCharCode(numeros);
        clabe= clabe+numeros_random;
    }
    return clabe;
}

console.log(generarClabe2()); 