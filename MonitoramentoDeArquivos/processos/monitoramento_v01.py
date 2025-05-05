import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from graphviz import Digraph
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        logger.info(f"Arquivo criado: {event.src_path}")
        # Processamento adicional aqui

    def on_modified(self, event):
        logger.info(f"Arquivo modificado: {event.src_path}")
        # Processamento adicional aqui

    def on_deleted(self, event):
        logger.info(f"Arquivo deletado: {event.src_path}")
        # Processamento adicional aqui

class DirectoryWatcher:
    def __init__(self, directory, next_directory=None):
        self.directory = directory
        self.next_directory = next_directory
        self.observer = Observer()

    def run(self):
        event_handler = FileEventHandler(self.directory, self.next_directory)
        self.observer.schedule(event_handler, self.directory, recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

class FileEventHandler(FileSystemEventHandler):
    def __init__(self, current_directory, next_directory):
        self.current_directory = current_directory
        self.next_directory = next_directory

    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith('.txt'):
            file_name = os.path.basename(event.src_path)
            print(f"Detected {file_name} in {self.current_directory}")
            self.process_file(file_name)

    def process_file(self, file_name):
        # Simulate processing
        time.sleep(2)  # Simulate some processing time.
        new_path = os.path.join(self.next_directory, file_name) if self.next_directory else None
        if new_path:
            original_path = os.path.join(self.current_directory, file_name)
            os.rename(original_path, new_path)
            print(f"Moved {file_name} to {self.next_directory}")
            self.update_diagram(self.current_directory, self.next_directory, file_name)

    def update_diagram(self, current_directory, next_directory, file_name):
        dot = Digraph(comment='Fluxo de Documentos Detalhado')
        dot.node(current_directory, current_directory)
        if next_directory:
            dot.node(next_directory, next_directory)
            dot.edge(current_directory, next_directory, label=file_name)
        dot.render('process_flow', format='png', view=True)


def main():
    log = Handler()
    DIRECTORY_TO_WATCH = "C:\\xampp2\\htdocs\\python_aulas\\MonitoramentoDeArquivos"
    paths = ["entrada", "fase1", "fase2", "fase3", "saída"]
    full_paths = [os.path.join(DIRECTORY_TO_WATCH, "processos", path) for path in paths]
    watchers = [DirectoryWatcher(full_paths[i], full_paths[i + 1]) for i in range(len(full_paths) - 1)]
    watchers.append(DirectoryWatcher(full_paths[-1]))  # Last directory has no next directory

    for watcher in watchers:
        watcher.run()

if __name__ == "__main__":
    main()