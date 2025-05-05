from abc import ABC, abstractmethod
class FileSystemComponent(ABC):
    @abstractmethod
    def show_details(self):
        pass
#leaf
class File(FileSystemComponent):
    def __init__(self,nome):
        self.nome = nome
    def show_details(self):
        print(f"File:{self.nome}")
#composite        
class Directory(FileSystemComponent):
    def __init__(self,nome):
        self.nome = nome
        self.components = []
    
    def add(self,component):
        self.components.append(component)
    
    def remove(self,component):
        self.components.append(component)

    def show_details(self):
        print(f"Diretory:{self.nome}")
        for component in self.components:
            component.show_details()

if __name__=="__main__":
    arq1 = File("File1.txt")
    arq2 = File("File2.txt")
    arq3 = File("File3.txt")
    dir1 = Directory("Dir1")
    dir2 = Directory("Dir2")

    dir1.add(arq1)
    dir1.add(arq2)
    dir2.add(arq3)
    root = Directory("root")
    root.add(dir1)
    root.add(dir2)
    root.show_details()
