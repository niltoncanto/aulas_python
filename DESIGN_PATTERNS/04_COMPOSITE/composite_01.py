from abc import ABC, abstractmethod
# Component
class FileSystemComponent(ABC):
    @abstractmethod
    def show_details(self) -> None:
        pass
# Leaf
class File(FileSystemComponent):
    def __init__(self, name: str) -> None:
        self.name = name

    def show_details(self) -> None:
        print(f"File: {self.name}")
# Composite
class Directory(FileSystemComponent):
    def __init__(self, name: str) -> None:
        self.name = name
        self._components = []
    def add(self, component: FileSystemComponent) -> None:
        self._components.append(component)
    def remove(self, component: FileSystemComponent) -> None:
        self._components.remove(component)
    def show_details(self) -> None:
        print(f"Directory: {self.name}")
        for component in self._components:
            component.show_details()
# Client code
if __name__ == "__main__":
    file1 = File("File1.txt")
    file2 = File("File2.txt")
    file3 = File("File3.txt")
    dir1 = Directory("Dir1")
    dir2 = Directory("Dir2")
    dir1.add(file1)
    dir1.add(file2)
    dir2.add(file3)
    root = Directory("Root")
    root.add(dir1)
    root.add(dir2)
    root.show_details()
