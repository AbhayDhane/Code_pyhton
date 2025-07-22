import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Folder to monitor (Downloads folder)
SOURCE_DIR = os.path.expanduser("~/Downloads")

# Destination subfolders based on file types
DESTINATIONS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Apps": [".exe", ".msi", ".apk"]
}

def get_destination(file_name):
    _, ext = os.path.splitext(file_name)
    for folder, extensions in DESTINATIONS.items():
        if ext.lower() in extensions:
            return os.path.join(SOURCE_DIR, folder)
    return os.path.join(SOURCE_DIR, "Others")

class FileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for file in os.listdir(SOURCE_DIR):
            file_path = os.path.join(SOURCE_DIR, file)
            if os.path.isfile(file_path):
                dest_folder = get_destination(file)
                os.makedirs(dest_folder, exist_ok=True)
                try:
                    shutil.move(file_path, os.path.join(dest_folder, file))
                    print(f"📦 Moved: {file} → {dest_folder}")
                except Exception as e:
                    print(f"❌ Error moving {file}: {e}")

if __name__ == "__main__":
    print(f"🔍 Monitoring: {SOURCE_DIR}")
    observer = Observer()
    event_handler = FileHandler()
    observer.schedule(event_handler, SOURCE_DIR, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
