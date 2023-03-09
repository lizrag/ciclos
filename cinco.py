# --5)Un numero de tarjeta bancaria esta formada de 16 digitos, genere un metodo
# que retorne o devuelva un numero con 16 digitos al azar para este metodo
# utilice el codigo ascii para obtener los numeros aleatorios, este metodo
# debe nombrarse generaNumeroTarjeta()

list_1 = ["C/43243&","C/43243&", "C/43243&" ]
list_2 = ["C/43243&","C/43243", "C/43243w"]

dict1 = dict(zip(list_1, list_2))
print(dict1)

diccionario = {}
list = []
for i, valor in enumerate(list_1):
    diccionario[valor] = list_2[i]
    print(diccionario)