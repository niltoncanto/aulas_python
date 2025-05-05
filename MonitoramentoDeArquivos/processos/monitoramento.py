# .env\Scripts\activate
# python -m venv .env
# pip install virtualenv
# pip install networkx
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

class DirectoryWatcher:
    def __init__(self, directory, next_directory=None):
        self.directory = directory
        self.next_directory = next_directory
        self.observer = Observer()
        self.event_handler = FileEventHandler(self.directory, self.next_directory, self.observer, self)

    def run(self):
        self.observer.schedule(self.event_handler, self.directory, recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

class FileEventHandler(FileSystemEventHandler):
    def __init__(self, current_directory, next_directory, observer, directory_watcher):
        self.current_directory = current_directory
        self.next_directory = next_directory
        self.observer = observer
        self.directory_watcher = directory_watcher

    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith('.txt'):
            file_name = os.path.basename(event.src_path)
            logger.info(f"Detected {file_name} in {self.current_directory}")
            self.process_file(file_name)

    def process_file(self, file_name):
        original_path = os.path.join(self.current_directory, file_name)
        if self.next_directory:
            new_path = os.path.join(self.next_directory, file_name)
            if os.path.exists(original_path):
                os.rename(original_path, new_path)
                logger.info(f"Moved {file_name} to {self.next_directory}")
                # Reconfigure the observer to monitor the new directory
                self.observer.unschedule_all()
                self.directory_watcher.next_directory = self.next_directory
                self.observer.schedule(self, self.next_directory, recursive=False)
            else:
                logger.error(f"File not found: {original_path}")

def main():
    DIRECTORY_TO_WATCH = "C:\\xampp2\\htdocs\\python_aulas\\MonitoramentoDeArquivos\\processos"
    paths = ["entrada", "fase1", "fase2", "fase3", "saída"]
    full_paths = [os.path.join(DIRECTORY_TO_WATCH, path) for path in paths]
    directory_watchers = []
    for i in range(len(full_paths) - 1):
        watcher = DirectoryWatcher(full_paths[i], full_paths[i + 1])
        directory_watchers.append(watcher)
        watcher.run()

if __name__ == "__main__":
    main()
