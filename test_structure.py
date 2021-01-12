from structure import File, Folder, IncorrectSizeError
import pytest


def test_create_folder():
    home = Folder('home')
    assert home.name == 'home'
    assert home.size == 0
    assert home.content == []
    assert home.directory is None


def test_create_folder_with_content():
    laby = Folder('laby')
    lab10 = File(laby, 'lab10', 'py', 100)
    laby_copy = Folder('laby_copy', None, [lab10], laby.size)
    assert laby_copy.name == 'laby_copy'
    assert laby_copy.directory is None
    assert laby_copy.content[0] == lab10
    assert laby_copy.size == 100


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


def test_file_type():
    home = Folder('home')
    file = File(home, 'file', 'txt', 1000)
    assert file.type() == 'txt'


def test_str_file():
    home = Folder('home')
    lab10 = File(home, 'lab10', 'py', 100)
    description = str(lab10)
    assert description == 'Name:lab10 Type:py Size:100 In directory: home'


def test_copy_file_into_working_dir():
    home = Folder('home')
    lab10 = File(home, 'lab10', 'py', 100)
    assert len(home.content) == 1
    lab10.copy(home, 'lab10_copy')
    if_copy_exists = True if len(home.content) == 2 else False
    assert if_copy_exists is True
    assert home.content[1].name == 'lab10_copy'
    assert home.content[1].size == lab10.size
    assert home.content[1]._type == lab10._type


def test_copy_file_to_another_dir():
    home = Folder('home')
    new_folder = Folder('new_folder')
    lab10 = File(home, 'lab10', 'py', 100)
    assert len(new_folder.content) == 0
    lab10.copy(new_folder, 'lab10_copy')
    if_copy_exists = True if len(new_folder.content) == 1 else False
    assert if_copy_exists is True
    assert new_folder.content[0].name == 'lab10_copy'
    assert new_folder.content[0].size == lab10.size
    assert new_folder.content[0]._type == lab10._type


def test_str_folder():
    home = Folder('home')
    description = str(home)
    assert description == "Folder name: home, size: 0"


def test_folder_size():
    home = Folder('home')
    lab10 = File(home, 'lab10', 'py', 100)
    lab11 = File(home, 'lab11', 'py', 200)
    lab12 = File(home, 'lab12', 'py', 1)
    assert home.size == 301


def test_folder_count_size_recursive():
    home = Folder('home')
    lab10 = File(home, 'lab10', 'py', 100)
    lab11 = File(home, 'lab11', 'py', 200)
    project = Folder('project', home)
    file1 = File(project, 'file1', 'py', 100)
    file2 = File(project, 'file2', 'py', 150)
    size = home.count_size_recursive()
    assert size == 550


def test_folder_add_element():
    home = Folder('home')
    user_one = Folder('user_one')
    file = File(user_one, 'file', 'exe', 1510)
    assert home.size == 0
    assert home.content == []
    home.add_element(file)
    assert len(home.content) == 1
    assert home.size == 1510


def test_folder_delete_element():
    home = Folder('home')
    file = File(home, 'file', 'exe', 1510)
    assert home.size == 1510
    assert len(home.content) == 1
    home.delete_element(file)
    assert home.size == 0
    assert home.content == []


# def test_folder_list_elements():
#     home = Folder('home')
#     file1 = File(home, 'file1', 'txt', 1000)
#     folder1= Folder('folder1', home)
#     file2 = File(folder1, 'file2', 'txt', 1000)
#     tree = "home/n file1/n folder1/n  file2"
#     treee = home.list_elements()
#     assert tree == treee


def test_folder_find_file():
    home = Folder('home')
    file1 = File(home, 'file1', 'txt', 1000)
    folder1 = Folder('folder1', home)
    file2 = File(folder1, 'file2', 'txt', 1000)
    wanted = home.find('file2')
    assert wanted == file2


def test_folder_find_itself():
    home = Folder('home')
    file1 = File(home, 'file1', 'txt', 1000)
    folder1 = Folder('folder1', home)
    file2 = File(folder1, 'file2', 'txt', 1000)
    wanted = home.find('home')
    assert wanted == home


def test_folder_find_folder():
    home = Folder('home')
    file1 = File(home, 'file1', 'txt', 1000)
    folder1= Folder('folder1', home)
    file2 = File(folder1, 'file2', 'txt', 1000)
    wanted = home.find('folder1')
    assert wanted == folder1


def test_folder_find_no_matches():
    home = Folder('home')
    file1 = File(home, 'file1', 'txt', 1000)
    folder1 = Folder('folder1', home)
    file2 = File(folder1, 'file2', 'txt', 1000)
    wanted = home.find('fileX')
    assert wanted is None


def test_copy_folder():
    home = Folder('home')
    movies = Folder('movies')
    movie = File(movies, 'movie', 'mp4', 1510)
    assert home.content == []
    movies.copy(home, 'movies_copy')
    assert len(home.content) == 1
    assert home.content[0].name == 'movies_copy'


def test_copy_file():
    home = Folder('home')
    movies = Folder('movies')
    movie = File(movies, 'movie', 'mp4', 1510)
    assert home.content == []
    movies.copy(home, 'movies_copy')
    assert len(home.content) == 1
    assert home.content[0].name == 'movies_copy'


def test_folder_count_elements():
    pictures = Folder('pictures')
    pic_1 = File(pictures, 'pic_1', 'jpg', 999)
    pic_2 = File(pictures, 'pic_2', 'jpg', 999)
    pic_3 = File(pictures, 'pic_3', 'jpg', 999)
    pic_4 = File(pictures, 'pic_4', 'jpg', 999)
    assert pictures.count_elements() == 4


def test_folder_count_elements_recursive():
    pictures = Folder('pictures')
    pic_1 = File(pictures, 'pic_1', 'jpg', 999)
    pic_2 = File(pictures, 'pic_2', 'jpg', 999)
    pic_3 = File(pictures, 'pic_3', 'jpg', 999)
    holiday = Folder('holiday', pictures)
    pic_4 = File(holiday, 'pic_4', 'jpg', 999)
    pic_5 = File(holiday, 'pic_5', 'jpg', 999)
    assert pictures.count_elements_recursive() == 6


def test_folder_count_only_files():
    pictures = Folder('pictures')
    pic_1 = File(pictures, 'pic_1', 'jpg', 999)
    pic_2 = File(pictures, 'pic_2', 'jpg', 999)
    pic_3 = File(pictures, 'pic_3', 'jpg', 999)
    holiday = Folder('holiday', pictures)
    assert pictures.count_only_files() == 3


def test_count_only_files_recursive():
    pictures = Folder('pictures')
    pic_1 = File(pictures, 'pic_1', 'jpg', 999)
    pic_2 = File(pictures, 'pic_2', 'jpg', 999)
    pic_3 = File(pictures, 'pic_3', 'jpg', 999)
    holiday = Folder('holiday', pictures)
    pic_4 = File(holiday, 'pic_4', 'jpg', 999)
    pic_5 = File(holiday, 'pic_5', 'jpg', 999)
    assert pictures.count_only_files_recursive() == 5
