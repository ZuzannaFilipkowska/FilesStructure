from structure import File, Folder
from commands import cd, cp, mv, cat, wc


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
    answer = "cd home/folder2".split()
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
    home = Folder('home')
    working_dir = Folder('working_dir')
    working_dir = home
    assert cd("cd a", working_dir, home) is None


# def test_rm_command(monkeypatch):
#     home = Folder('home')
#     working_dir = Folder('working_dir')
#     working_dir = home
#     folder1 = Folder('folder1', home)
#     file1 = File(home, 'file1', 'txt', 1000)
#     assert len(home.content) == 2
#     rm('file10', working_dir)
#     assert len(home.content) == 1


def test_get_path():
    pass


def test_cat_folder():
    home = Folder('home')
    working_dir = Folder('working_dir')
    working_dir = home
    folder1 = Folder('folder1', home)
    file1 = File(folder1, 'file1', 'txt', 1000)
    assert cat(working_dir, 'folder1') == str(folder1)


def test_cat_file():
    home = Folder('home')
    working_dir = Folder('working_dir')
    working_dir = home
    file1 = File(home, 'file1', 'txt', 1000)
    assert cat(working_dir, 'file1') == str(file1)


def test_copy_folder_to_working_dir():
    home = Folder('home')
    working_dir = Folder('working_dir')
    working_dir = home
    folder1 = Folder('folder1', home)
    File(folder1, 'file1', 'txt', 10)
    request = 'cp folder1 folder1_copy'.split()
    assert len(home.content) == 1
    cp(working_dir, request, home)
    assert len(home.content) == 2
    assert home.content[1].name == "folder1_copy"


def test_copy_file_to_working_dir():
    home = Folder('home')
    working_dir = Folder('working_dir')
    working_dir = home
    folder1 = Folder('folder1', home)
    File(folder1, 'file1', 'txt', 10)
    request = 'cp file1 file1_copy'.split()
    assert len(home.content) == 1
    cp(working_dir, request, home)
    assert len(home.content) == 2
    assert home.content[1].name == "file1_copy"


def test_copy_folder_to_another_folder():
    home = Folder('home')
    working_dir = Folder('working_dir')
    working_dir = home
    folder1 = Folder('folder1', home)
    folder2 = Folder("folder2", home)
    request = 'cp folder1 folder2 folder1_copy'.split()
    assert len(folder2.content) == 0
    cp(working_dir, request, home)
    assert len(folder2.content) == 1
    assert folder2.content[0].name == "folder1_copy"


def test_copy_folder_to_another_folder_with_path():
    home = Folder('home')
    working_dir = Folder('working_dir')
    working_dir = home
    folder1 = Folder('folder1', home)
    folder2 = Folder("folder2", home)
    request = 'cp folder1 home/folder2 folder1_copy'.split()
    assert len(folder2.content) == 0
    cp(working_dir, request, home)
    assert len(folder2.content) == 1
    assert folder2.content[0].name == "folder1_copy"


def test_move_folder_to_working_dir():
    home = Folder('home')
    working_dir = Folder('working_dir')
    working_dir = home
    folder1 = Folder('folder1', home)
    File(folder1, 'file1', 'txt', 10)
    request = 'mv folder1 folder1_copy'.split()
    assert len(home.content) == 1
    mv(working_dir, request, home)
    assert len(home.content) == 1
    assert home.content[0].name == "folder1_copy"


def test_move_file_to_working_dir():
    home = Folder('home')
    working_dir = Folder('working_dir')
    working_dir = home
    folder1 = Folder('folder1', home)
    File(folder1, 'file1', 'txt', 10)
    assert len(home.content) == 1
    request = 'mv file1 file1_copy'.split()
    mv(working_dir, request, home)
    assert len(home.content) == 2
    assert len(folder1.content) == 0
    assert home.content[1].name == "file1_copy"


def test_move_folder_to_another_folder():
    home = Folder('home')
    working_dir = Folder('working_dir')
    working_dir = home
    folder1 = Folder('folder1', home)
    folder2 = Folder("folder2", home)
    request = 'mv folder1 folder2 folder1_copy'.split()
    assert len(folder2.content) == 0
    assert len(home.content) == 2
    mv(working_dir, request, home)
    assert len(folder2.content) == 1
    assert len(home.content) == 1
    assert folder2.content[0].name == "folder1_copy"


def test_move_folder_to_another_folder_with_path():
    home = Folder('home')
    working_dir = Folder('working_dir')
    working_dir = home
    folder1 = Folder('folder1', home)
    folder2 = Folder("folder2", home)
    request = 'mv folder1 home/folder2 folder1_copy'.split()
    assert len(home.content) == 2
    assert len(folder2.content) == 0
    mv(working_dir, request, home)
    assert len(folder2.content) == 1
    assert len(home.content) == 1
    assert folder2.content[0].name == "folder1_copy"


def test_folder_wc():
    pictures = Folder('pictures')
    pic_1 = File(pictures, 'pic_1', 'jpg', 999)
    pic_2 = File(pictures, 'pic_2', 'jpg', 999)
    pic_3 = File(pictures, 'pic_3', 'jpg', 999)
    request = "wc pictures".split()
    num_of_elements = wc(pictures, request)
    assert num_of_elements == 3


def test_folder_wc_only_files():
    pictures = Folder('pictures')
    pic_1 = File(pictures, 'pic_1', 'jpg', 999)
    pic_2 = File(pictures, 'pic_2', 'jpg', 999)
    pic_3 = File(pictures, 'pic_3', 'jpg', 999)
    holiday = Folder("holiday", pictures)
    request = "wc -f pictures".split()
    num_of_elements = wc(pictures, request)
    assert num_of_elements == 3


def test_folder_wc_recursive():
    pictures = Folder('pictures')
    pic_1 = File(pictures, 'pic_1', 'jpg', 999)
    pic_2 = File(pictures, 'pic_2', 'jpg', 999)
    pic_3 = File(pictures, 'pic_3', 'jpg', 999)
    holiday = Folder('holiday', pictures)
    pic_4 = File(holiday, 'pic_4', 'jpg', 999)
    pic_5 = File(holiday, 'pic_5', 'jpg', 999)
    request = "wc -r pictures".split()
    num_of_elements = wc(pictures, request)
    assert num_of_elements == 6


def test_folder_wc_only_files_recursive():
    pictures = Folder('pictures')
    pic_1 = File(pictures, 'pic_1', 'jpg', 999)
    pic_2 = File(pictures, 'pic_2', 'jpg', 999)
    pic_3 = File(pictures, 'pic_3', 'jpg', 999)
    holiday = Folder('holiday', pictures)
    pic_4 = File(holiday, 'pic_4', 'jpg', 999)
    pic_5 = File(holiday, 'pic_5', 'jpg', 999)
    request = "wc -r -f pictures".split()
    num_of_elements = wc(pictures, request)
    assert num_of_elements == 5


