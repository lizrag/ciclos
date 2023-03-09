# --1)Una CLABE interbancaria esta formada de 18 digitos, genere un metodo
# que retorne o devuelva un numero con 18 digitos al azar para este metodo
# utilice el codigo ascii para obtener los numeros aleatorios, este metodo
# debe nombrarse generaCLABE()
import random

def generarCLABE():
    clabe = ""
    for i in range(19):
        numeros = random.randint(48,57)
        numeros_random = chr(numeros)
        clabe = clabe + numeros_random
    return clabe

print(generarCLABE())