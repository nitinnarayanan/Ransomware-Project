from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

import time
import logging

logging.basicConfig(level=logging.INFO, format ='%(asctime)s - %(message)s', datefmt='%m-%d-%Y  %H:%M:%S')

path = "/home/sec-lab/Desktop/Project_Environment_Folder/"

event_Handler = LoggingEventHandler()

observer = Observer()
observer.schedule(event_Handler, path, recursive = True )
observer.start()

try:
    while True:
        time.sleep(1)
finally:
    observer.stop()
    observer.join()

