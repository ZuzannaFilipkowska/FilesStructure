from structure import File, Folder
from main import cd

def test_function_cd():
    home = Folder('home')
    working_dir = Folder('working_dir')
    working_dir = home

    plik1 = File(home, 'plik1', 'txt', 1)
    plik2 = File(home, 'plik2', 'txt', 2)
    folder1 = Folder('folder1', home)
    plik3 = File(folder1, 'plik3', 'txt', 3)
    answer = "cd folder1".split()
    working_dir = cd(answer, working_dir, home)
    assert working_dir.name == 'folder1'
