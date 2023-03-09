import os

ruta_principal = "C:/Users/laura/OneDrive/Documents/prueba/"
def obtener_rutas_de_carpetas(ruta):
    rutas = [os.path.join(ruta, carpeta) for carpeta in os.listdir(ruta) if os.path.isdir(os.path.join(ruta,carpeta))]
    nombres = [os.path.join(carpeta) for carpeta in os.listdir(ruta) if os.path.isdir(os.path.join(ruta, carpeta))]
    return rutas, nombres

#rutas, nombres = obtener_rutas_de_carpetas(ruta_principal)

def routes_metadata(rutas, nombres):
    my_list = []
    i = 0
    while i < len(rutas) and i < len(nombres):
        my_dict = {}
        my_dict['ruta'] = rutas[i]
        my_dict['nombre'] = nombres[i]

        my_list.append(my_dict)
        i+=1
        #print(my_list)
    return my_list


def format_route(ruta):
    ruta_ext = ruta.split('\\')[:-1]
    ruta_ext = '\\'.join(ruta_ext)
    return ruta_ext


#print("Starting")