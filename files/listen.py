from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

def created(event):
    if event.is_directory:
        print("A folder created")

    print(f'{event.src_path} has been created')

def modified(event):
    if event.is_directory:
        print("A folder modified")

    print(f'{event.src_path} has been modified')

def deleted(event):
    if event.is_directory:
        print("A folder created")

    print(f'{event.src_path} has been deleted')


if __name__ == '__main__':
    path = 'D:/code/python/test'

    observer = Observer()
    event_handler = FileSystemEventHandler()

    event_handler.on_created = created
    event_handler.on_deleted = deleted
    event_handler.on_modified = modified
    observer.schedule(event_handler,path,recursive=True)

    observer.start()

    try:
        time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

