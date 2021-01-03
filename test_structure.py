from structure import File, Folder
from main import cd, rm, count


def test_create_file():
    home = Folder('home')
    lab10 = File(home, 'lab10', 'py', 100)
    assert lab10.name == 'lab10'
    assert lab10._type == 'py'
    assert lab10.size == 100
    assert lab10.directory == home


def test_str_file():
    pass


def test_create_folder():
    home = Folder('home')
    assert home.name == 'home'
    assert home.size == 0


def test_create_folder_with_content():
    laby = Folder('laby')
    lab10 = File(laby, 'lab10', 'py', 100)
    laby_copy = Folder('laby_copy', None, [lab10])
    assert laby_copy.name == 'laby_copy'
    assert laby_copy.content[0] == lab10
    assert laby_copy.size == 100


def test_str_folder():
    pass


def test_folder_size():
    pass


def test_command_cd_without_slash():
    home = Folder('home')
    working_dir = Folder('working_dir')
    working_dir = home
    folder1 = Folder('folder1', home)
    answer = "cd folder1".split()
    working_dir = cd(answer, working_dir, home)
    assert working_dir.name == 'folder1'


def test_command_cd_with_slash():
    home = Folder('home')
    working_dir = Folder('working_dir')
    working_dir = home
    folder1 = Folder('folder1', home)
    folder2 = Folder('folder2', home)
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


def test_make_directory():
    pass

# czy jest sens pisać takie testy?


def test_make_file():
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


def test_count():
    home = Folder('home')
    working_dir = Folder('working_dir')
    working_dir = home
    file1 = File(home, 'file1', 'txt', 1000)
    file2 = File(home, 'file2', 'txt', 1000)
    file3 = File(home, 'file3', 'txt', 1000)
    number = count(working_dir, 'home')
    assert number == 3


def test_count_file():
    home = Folder('home')
    working_dir = Folder('working_dir')
    working_dir = home
    file1 = File(home, 'file1', 'txt', 1000)
    file2 = File(home, 'file2', 'txt', 1000)
    file3 = File(home, 'file3', 'txt', 1000)
    number = count(working_dir, 'file1')
    assert number == 0
