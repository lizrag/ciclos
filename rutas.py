import os

# ruta_principal = "C:/Users/marco/OneDrive/Escritorio/NodeJS/"
def obtener_rutas_de_carpetas(ruta, nombre=None):
    rutas = [
        os.path.join(ruta, carpeta) 
        for carpeta in os.listdir(ruta) 
        if (
            os.path.isdir(os.path.join(ruta, carpeta)) 
            and (nombre is None or nombre in carpeta)
        )
    ]
        
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
    new_route = ruta.split('\\')[:-1]
    new_route = '\\'.join(new_route)

    return new_route


def get_files(ruta):
    # extension = ('.VAR', '.FIL', '.TDR')
    extension = ('.txt', '.docx')
    files = os.listdir(ruta)
    txt_files = [file for file in files if file.endswith(extension)]

    return txt_files


# print(get_files('C:/Users/marco/OneDrive/Escritorio/NodeJS/server_a'))