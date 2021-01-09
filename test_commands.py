from structure import File, Folder
from commands import cd, cp_mv


def test_command_cd_without_slash():
    home = Folder('home')
    working_dir = Folder('working_dir')
    working_dir = home
    Folder('folder1', home)
    answer = "cd folder1".split()
    working_dir = cd(answer, working_dir, home)
    assert working_dir.name == 'folder1'


def test_command_cd_with_slash():
    home = Folder('home')
    working_dir = Folder('working_dir')
    working_dir = home
    Folder('folder1', home)
    Folder('folder2', home)
    answer = "cd folder1".split()
    working_dir = cd(answer, working_dir, home)
    assert working_dir.name == 'folder1'
    answer = "cd /home/folder2".split()
    working_dir = cd(answer, working_dir, home)
    assert working_dir.name == 'folder2'


def test_command_cd_go_to_home():
    home = Folder('home')
    working_dir = Folder('working_dir')
    working_dir = home
    folder1 = Folder('folder1', home)
    folder2 = Folder('folder2', home)
    folder3 = Folder('folder3', folder1)
    answer = "cd folder1".split()
    working_dir = cd(answer, working_dir, home)
    assert working_dir.name == 'folder1'
    answer = "cd folder3".split()
    working_dir = cd(answer, working_dir, home)
    assert working_dir.name == 'folder3'
    answer = "cd".split()
    working_dir = cd(answer, working_dir, home)
    assert working_dir.name == 'home'


def test_command_cd_go_folder_up():
    home = Folder('home')
    working_dir = Folder('working_dir')
    working_dir = home
    folder1 = Folder('folder1', home)
    folder2 = Folder('folder2', home)
    folder3 = Folder('folder3', folder1)
    answer = "cd folder1".split()
    working_dir = cd(answer, working_dir, home)
    assert working_dir.name == 'folder1'
    answer = "cd folder3".split()
    working_dir = cd(answer, working_dir, home)
    assert working_dir.name == 'folder3'
    answer = "cd ..".split()
    working_dir = cd(answer, working_dir, home)
    assert working_dir.name == 'folder1'


def test_command_cd_incorrect_folder():
    pass


def test_rm_command():
    home = Folder('home')
    working_dir = Folder('working_dir')
    working_dir = home
    folder1 = Folder('folder1', home)
    file1 = File(home, 'file1', 'txt', 1000)
    assert len(home.content) == 2
    rm('file1', working_dir)
    assert len(home.content) == 1


# def test_count():
#     home = Folder('home')
#     working_dir = Folder('working_dir')
#     working_dir = home
#     file1 = File(home, 'file1', 'txt', 1000)
#     file2 = File(home, 'file2', 'txt', 1000)
#     file3 = File(home, 'file3', 'txt', 1000)
#     number = count(working_dir, 'home')
#     assert number == 3


# def test_count_file():
#     home = Folder('home')
#     working_dir = Folder('working_dir')
#     working_dir = home
#     file1 = File(home, 'file1', 'txt', 1000)
#     file2 = File(home, 'file2', 'txt', 1000)
#     file3 = File(home, 'file3', 'txt', 1000)
#     number = count(working_dir, 'file1')
    # assert number == 0


def test_copy():
    home = Folder('home')
    working_dir = Folder('working_dir')
    working_dir = home
    folder1 = Folder('folder1', home)
    File(folder1, 'file1', 'txt', 10)
    request = 'cp folder1 folder1_copy'.split()
    cp_mv(working_dir, request, home, False)
    assert len(home.content) == 2
