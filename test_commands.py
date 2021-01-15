from structure import File, Folder
from commands import cd, cp, mv, cat, wc, ls, rm, get_path, help
from io import StringIO


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


def test_command_rm(monkeypatch):
    home = Folder('home')
    working_dir = Folder('working_dir')
    working_dir = home
    folder1 = Folder('folder1', home)
    file1 = File(home, 'file1', 'txt', 1000)
    assert len(home.content) == 2
    input_decision = StringIO('Y\n')
    monkeypatch.setattr('sys.stdin', input_decision)
    rm(file1, working_dir, home)
    assert len(home.content) == 1


def test_get_path():
    home = Folder('home')
    pictures = Folder('pictures', home)
    holiday = Folder('holiday', pictures)
    working_dir = holiday
    path = get_path(working_dir, home)
    assert path == "~/home/pictures/holiday "


def test_command_wc():
    pictures = Folder('pictures')
    pic_1 = File(pictures, 'pic_1', 'jpg', 999)
    pic_2 = File(pictures, 'pic_2', 'jpg', 999)
    pic_3 = File(pictures, 'pic_3', 'jpg', 999)
    request = "wc pictures".split()
    num_of_elements = wc(pictures, request)
    assert num_of_elements == 3


def test_command_wc_only_files():
    pictures = Folder('pictures')
    pic_1 = File(pictures, 'pic_1', 'jpg', 999)
    pic_2 = File(pictures, 'pic_2', 'jpg', 999)
    pic_3 = File(pictures, 'pic_3', 'jpg', 999)
    holiday = Folder("holiday", pictures)
    request = "wc -f pictures".split()
    num_of_elements = wc(pictures, request)
    assert num_of_elements == 3


def test_command_wc_recursive():
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


def test_command_wc_only_files_recursive():
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


def test_ls():
    pictures = Folder('pictures')
    pic_1 = File(pictures, 'pic_1', 'jpg', 999)
    pic_2 = File(pictures, 'pic_2', 'jpg', 999)
    pic_3 = File(pictures, 'pic_3', 'jpg', 999)
    holiday = Folder('holiday', pictures)
    pic_4 = File(holiday, 'pic_4', 'jpg', 999)
    pic_5 = File(holiday, 'pic_5', 'jpg', 999)
    tree = """pictures
 -pic_1
 -pic_2
 -pic_3
  holiday
   -pic_4
   -pic_5"""
    request = "ls pictures".split()
    assert tree == ls(pictures, request)


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


def test_help():
    manual = """
        Commands list:

        cd - changes directory
            cd .. - moves one directory up
            cd - moves to home direcory
            cd [folder_name] or cd [path/to/folder] - moves to given folder

        ----------------------------------------------------------------

        mkdir - makes directory
            mk [directory name]

        ----------------------------------------------------------------

        mk - makes file
            mk [file name] [file type] [file size]

            enter size in kB

        ----------------------------------------------------------------

        cp - copy files or directories from working dir
            cp [origin] [destination] [name] - copy to given place
            cp [origin] [name] - copy to working dir
        ----------------------------------------------------------------

        mv - moves files or directories from working dir
            mv [original] [destination] [copy name] - copy to given place
            mv [original] [copy name] - copy to working directory
        ----------------------------------------------------------------

        rm - removes file/folder
            rm [to_be_deleted]

        ----------------------------------------------------------------
        ls - lists contents of directories in a tree-like format
            ls - lists content od working directory
            ls [folder name] - lists content of folder
        ----------------------------------------------------------------

        cat - prints file/folder information
            cat [element name]

        ----------------------------------------------------------------

        size - prints size of folder, counted recursively
            size [folder name]

        ----------------------------------------------------------------
        wc - counts elements, by default with depth=1
            wc [option] [option] [folder name]

           OPTIONS:
           -r - counts recursively
           -f - counts only files

        ----------------------------------------------------------------

        pwd - prints working directory name
            pwd

        ----------------------------------------------------------------

        exit - ends program

    """
    assert help() == manual
