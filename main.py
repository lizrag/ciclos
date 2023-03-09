from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from rutas import obtener_rutas_de_carpetas, routes_metadata, format_route
from repo_sync import sync_data

origin_paths, origin_names = obtener_rutas_de_carpetas("C:/Users/laura/OneDrive/Documents/prueba/")
routes_origin = routes_metadata(origin_paths, origin_names)

dest_path, dest_names = obtener_rutas_de_carpetas("C:/Users/laura/OneDrive/Documents/")
routes_dest = routes_metadata(dest_path,dest_names)


class FileSystem(FileSystemEventHandler):
    def on_any_event(self, event):
        #print(event.src_path)
        new_route = format_route(event.src_path)
        folder_name = [diccionario['nombre'] for diccionario in routes_origin if diccionario['ruta'] == new_route]
        dest_folder = [diccionario['ruta'] for diccionario in routes_dest if diccionario['nombre'] == folder_name[0]]
        #print(new_route)
        print(str(dest_folder[0]))
        print("Se detectó el evento")
        sync_data(str(new_route), str(dest_folder[0]))

if __name__ == "__main__":
    event_handler = FileSystem()
    observer = Observer()
    for path in routes_origin:
        observer.schedule(event_handler, path = path['ruta'], recursive = True)
    observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


#print("Starting")