import os

ruta_principal = "C:/Users/marco/OneDrive/Escritorio/NodeJS/"
# elementos = os.listdir(ruta_principal)


def obtener_rutas_de_carpetas(ruta):
    rutas = [os.path.join(ruta, carpeta) for carpeta in os.listdir(ruta) if os.path.isdir(os.path.join(ruta, carpeta))]

    nombres = [os.path.join(carpeta) for carpeta in os.listdir(ruta) if os.path.isdir(os.path.join(ruta, carpeta))]

    return rutas, nombres

my_list = [
    
]



rutas, nombres = obtener_rutas_de_carpetas(ruta_principal)
print(rutas, nombres)

my_list = []
print(rutas, nombres)
i = 0
while i < len(rutas) and i < len(nombres):
    my_dict = {}    
    my_dict['ruta'] = rutas[i]
    my_dict['nombre'] = nombres[i]

    my_list.append(my_dict)
    i+=1
print(my_list)

# for ruta in rutas:
#     my_dict['ruta'] = ruta

#     my_list.append(my_dict)
# for nombre in nombres:
#     my_dict['nombre'] = nombre



# print(obtener_rutas_de_carpetas(ruta_principal))


# if carpetas_principales in carpetas_secundarias:
#     ejecutas shutil

lista_de_diccionarios = [
    {
    "origin": "ruta a",
    "destination": "ruta a"
    },
    {
    "origin": "ruta b",
    "destination": "ruta b"
    },
    {
    "origin": "ruta c",
    "destination": "ruta c"
    }
]
def move_files(origin, destination):
    '''proceso de shutils'''
    pass


for diccionario in lista_de_diccionarios:
    origin = diccionario['origin']
    destination = diccionario['destination']
    move_files(origin, destination)

