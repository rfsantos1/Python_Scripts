import os
import sys
import shutil
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler

source_dir=r"C:/Users/Murloc_Rampage/Downloads"
dest_dir_sfx=r"C:/Users/Murloc_Rampage/Downloads/SFX"
dest_dir_music=r"C:/Users/Murloc_Rampage/Downloads/Music"
dest_dir_images=r"C:/Users/Murloc_Rampage/Downloads/Images"
dest_dir_pdn=r"C:/Users/Murloc_Rampage/Downloads/Pdn"
dest_dir_videos=r"C:/Users/Murloc_Rampage/Downloads/Videos"
dest_dir_documents=r"C:/Users/Murloc_Rampage/Downloads/Docs"
dest_dir_text=r"C:/Users/Murloc_Rampage/Downloads/Text_Files"
dest_dir_zips=r"C:/Users/Murloc_Rampage/Downloads/zips"

def makeUnique(dest, name):
    filename, extension = os.path.splitext(name)
    counter = 1

    while os.path.exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter+=1

    return name

def move(dest, entry, name):
    if os.path.exists(f"{dest}/{name}"):
        unique_name = makeUnique(dest, name)
        oldName = os.path.join(dest, name)
        newName = os.path.join(dest, unique_name)
        os.rename(oldName, newName)
    shutil.move(entry,dest)

class MoverHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                dest = source_dir
                if name.endswith('.wav') or name.endswith('.mp3'):
                    if entry.stat().st_size < 25000000 or "SFX" in name:
                        dest=dest_dir_sfx
                    else:
                        dest=dest_dir_music
                    move(dest, entry, name)
                elif name.endswith('.mov') or name.endswith('.mp4'):
                    dest = dest_dir_videos
                    move(dest, entry, name)
                elif name.endswith('.jpg') or name.endswith('.jpeg') or name.endswith('.png'):
                    dest = dest_dir_images
                    move(dest, entry, name)
                elif name.endswith('.pdn'):
                    dest = dest_dir_pdn
                    move(dest, entry, name)
                elif name.endswith('.pdf') or name.endswith('.doc'):
                    dest = dest_dir_documents
                    move(dest, entry, name)
                elif name.endswith('.txt'):
                    dest = dest_dir_text
                    move(dest, entry, name)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()