# --3)Un numero de cuenta bancaria esta formada de 14 digitos, genere un metodo
# que retorne o devuelva un numero con 14 digitos al azar para este metodo
# utilice el codigo ascii para obtener los numeros aleatorios, este metodo
# debe nombrarse generaCuentaBancaria()
import random

def generaCuentaBancaria():
    cuenta = ""
    for i in range(14):
        numeros = random.randint(48,57)
        numeros_random = chr(numeros)
        cuenta = cuenta + numeros_random
    return cuenta

print(generaCuentaBancaria())