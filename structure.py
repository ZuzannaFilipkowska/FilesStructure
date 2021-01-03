class File:
    def __init__(self, directory, name, type, size):
        self.directory = directory
        self.name = name
        self._type = type
        self.size = int(size)
        directory.content.append(self)

    def __str__(self):
        return f'Name:{self.name} Type:{self._type} Size:{self.size} In directory: {self.directory}'


class Folder:
    def __init__(self, name, directory=None, content=None):
        self.content = [] if content is None else content
        self.name = name
        self.directory = directory
        self.size = int(self.count_size())
        if self.directory is not None:
            self.directory.content.append(self)

    def add_element(self, new_element):
        self.content.append(new_element)
        self.size += new_element.size

    def delete_element(self, element):
        self.content.remove(element)
        self.size -= element.size

    def count_size(self):
        size = 0
        for element in self.content:
            size += element.size
        return size

    def count_elements(self):
        return len(self.content)

    def list_elements(self, intend=0):
        print(intend * ' ' + self.name)
        intend += 1
        for element in self.content:
            if isinstance(element, File):
                print(intend * ' '+'-' + element.name)
            else:
                element.list_elements(intend + 1)
        return

    def __str__(self):
        print(f'Folder name: {self.name}, size: {self.size}')

    def find(self, name):
        if self.name == name:
            return self
        for element in self.content:
            if element.name == name:
                return element
            elif isinstance(element, Folder):
                element.find(name)


"""
program ma umożliwiać:
- usuwanie pl/fol
- kopiowanie fol/plikow
- przechodzenie po strukturze
- podglad plikow - czyli opis pliku
- zlczanie liczby plikow/folderow
- zliczanie rozmiaru folderu
"""
