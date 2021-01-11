class IncorrectSizeError(ValueError):
    pass


class File:
    """
    Class File. Contains attributes:
    :param directory: file source directory
    :type directory: Folder

    :param name: file name
    :type name: str

    :param type: file type
    :type type: str

    :param size: file size
    :type size: int
    """
    def __init__(self, directory, name, type, size):
        """
        Creates instance of File.
        """
        self.directory = directory
        self.name = str(name)
        self._type = type
        try:
            size = int(size)
            self.size = size
            if size < 0:
                raise IncorrectSizeError("Size must be a non-negative number")
        except ValueError:
            raise IncorrectSizeError("Size must be a non-negative number")
        self.directory.add_element(self)

    def __str__(self):
        """
        Returns basic description of the file.
        """
        description = f'Name:{self.name} Type:{self._type} Size:{self.size} In directory: {self.directory.name}'
        return description

    def type(self):
        """
        Return type of file.
        """
        return self._type

    def copy(self, copy_name, directory):
        """
        Creates copy of file in given directory.
        """
        copy_type = self.type()
        copy_size = self.size
        File(directory, copy_name, copy_type, copy_size)


class Folder:
    """
    Class Folder. Contains attributes:
    :param name: folder name
    :type name: str

    :param directory: folder source directory, defaults to None
    :type directory: Folder

    :param content: folder content, defaults to None
    :type content: list

    :param size: folder size, defaults to 0
    :type size: int
    """
    def __init__(self, name, directory=None, content=None, size=0):
        """
        Creates instance of Folder.
        """
        self.content = [] if content is None else content
        self.name = name
        self.directory = directory
        self.size = size  # sum of files sizes without files from subdir
        if self.directory is not None:
            self.directory.content.append(self)

    def add_element(self, new_element):
        """
        Adds element to folder content.
        """
        self.content.append(new_element)
        self.size += new_element.size

    def delete_element(self, element):
        """
        Removes element from folder content.
        Substracts element size from folder size.
        """
        self.content.remove(element)
        self.size -= element.size

    def list_elements(self, intend=0):
        """
        Prints directory tree.
        """
        print(intend * ' ' + self.name)
        intend += 1
        for element in self.content:
            if isinstance(element, File):
                print(intend * ' '+'-' + element.name)
            else:
                element.list_elements(intend + 1)
        return

    def find(self, name):
        """
        Searches for an object which has a given name.
        Returns found object if exists.
        """
        if self.name == name:
            return self
        for element in self.content:
            if element.name == name:
                return element
            elif isinstance(element, Folder):
                wanted = element.find(name)
                return wanted

    def copy(self, directory, copy_name):
        """
        Creates a copy of the folder in given directory.
        """
        copy_content = self.content
        copy_size = self.size
        Folder(copy_name, directory, copy_content, copy_size)

    def count_size_recursive(self):
        """
        Counts and returns size of the folder.
        """
        size = self.size
        for element in self.content:
            if isinstance(element, Folder):
                size += element.count_size_recursive()
        return size

    def count_elements(self):
        """
        Returns number of elements in folder content
        without counting elements in subdirectories.
        """
        return len(self.content)

    def count_elements_recursive(self):
        """
        Counts elements in folder content recursively and returns the value.
        """
        size = self.count_elements()
        for element in self.content:
            if isinstance(element, Folder):
                size += element.count_elements_recursive()
        return size

    def count_only_files(self):
        """
        Counts only files in folder content.
        Returns the value.
        """
        file_number = 0
        for element in self.content:
            if isinstance(element, File):
                file_number += 1
        return file_number

    def count_only_files_recursive(self, size=0):
        """
        Counts only files in folder content recursively.
        Return the value.
        """
        for element in self.content:
            if isinstance(element, File):
                size += 1
            else:
                size = element.count_only_files_recursive(size)
        return size

    def __str__(self):
        """
        Returns basic description of folder.
        """
        size = self.count_size_recursive()
        return (f'Folder name: {self.name}, size: {size}')
