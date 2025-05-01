import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            print(f"Dossier créé : {event.src_path}")
        else:
            print(f"Fichier créé : {event.src_path}")

    def on_deleted(self, event):
        if event.is_directory:
            print(f"Dossier supprimé : {event.src_path}")
        else:
            print(f"Fichier supprimé : {event.src_path}")

    def on_modified(self, event):
        if event.is_directory:
           print(f"Dossier modifié : {event.src_path}")
        else:
            print(f"Fichier modifié : {event.src_path}")

if __name__ == "__main__":
    path_to_watch = "D:\Test"  # Remplacez par le chemin du dossier à surveiller
    event_handler = MyEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path_to_watch, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
