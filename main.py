from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from rutas import obtener_rutas_de_carpetas, routes_metadata, format_route, get_files
from repo_sync import sync_data

origin = "C:/Users/marco/OneDrive/Escritorio/NodeJS/"
rutas_o, nombres_o = obtener_rutas_de_carpetas(origin)
rutas_origen = routes_metadata(rutas_o, nombres_o)

destination = "C:/Users/marco/OneDrive/Escritorio/CursoPy/"
# rutas_d, nombres_d = obtener_rutas_de_carpetas(destination)
# rutas_destino = routes_metadata(rutas_d, nombres_d)



class FileSystem(FileSystemEventHandler):
    def on_any_event(self, event):
        print(event)
        
        route = format_route(event.src_path)
        print(route)
        origin_folder_name = [diccionario['nombre'] for diccionario in rutas_origen if diccionario['ruta'] == route]
        # origin_folder_name = []
        # for diccionario in rutas_origen:
        #     if diccionario['ruta'] == route:
        #         origin_folder_name.append(diccionario['nombre'])
        # print(origin_folder_name)

        rutas_dest, nombres_dest = obtener_rutas_de_carpetas(destination, origin_folder_name[0])
        print(rutas_dest)

        files = get_files(route)
        # complete_route = route +'/' + file
        print(files)
        # sync_files = [sync_data(route+'/'+file, rutas_dest[0]) for file in files]
        sync_files = [route+'/'+file for file in files]
        final_routes = [sync_data(file, rutas_dest[0]) for file in sync_files]
        print(final_routes)

        print("Se detectó el evento")
        # sync_data(route, 'C:/Users/marco/OneDrive/Escritorio/CursoPy/server_a')

if __name__ == "__main__":
    event_handler = FileSystem()
    observer = Observer()
    for ruta in rutas_origen:
        observer.schedule(event_handler, path = ruta['ruta'], recursive = True)
    observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


#print("Starting")