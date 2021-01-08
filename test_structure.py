from structure import File, Folder, IncorrectSizeError
import pytest


def test_create_file():
    home = Folder('home')
    lab10 = File(home, 'lab10', 'py', 100)
    assert lab10.name == 'lab10'
    assert lab10._type == 'py'
    assert lab10.size == 100
    assert lab10.directory == home


def test_create_file_incorrect_size():
    home = Folder('folder')
    with pytest.raises(IncorrectSizeError):
        File(home, 'file', 'txt', 'abc')
        File(home, "file_b", 'csv', -10)


def test_str_file():
    pass


def test_create_folder():
    home = Folder('home')
    assert home.name == 'home'
    assert home.size == 0


def test_create_folder_with_content():
    laby = Folder('laby')
    lab10 = File(laby, 'lab10', 'py', 100)
    laby_copy = Folder('laby_copy', None, [lab10], laby.size)
    assert laby_copy.name == 'laby_copy'
    assert laby_copy.content[0] == lab10
    assert laby_copy.size == 100


def test_str_folder():
    pass


def test_folder_size():
    pass


def test_make_directory():
    pass

# czy jest sens pisać takie testy?


def test_make_file():
    home = Folder('home')
    file1 = File(home, 'file1', 'txt', 1)
    assert file1.size == 1
    assert home.size == 1
