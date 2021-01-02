from structure import Folder


def cd(answer, working_dir, home):
    if len(answer) == 1:
        # go to the home folder
        working_dir = home
        return working_dir
    elif answer[1] == "..":
        # move one directory up
        working_dir = working_dir.directory
        return working_dir
    else:
        # go to given directory
        given_folder = answer[1]
        if given_folder[0] == '/':
            path = given_folder.split('/')[1:]
            working_dir = home
            for i in range(0, len(path)-1):
                working_dir = working_dir.find(path[i+1])
            return working_dir
        else:
            working_dir = working_dir.find(given_folder)
            return working_dir


def rm(to_be_deleted, working_dir):
    """
    Removes given folder or file from working directory.
    """
    to_be_deleted = working_dir.find(to_be_deleted)
    if isinstance(to_be_deleted, Folder):
        decision = input("Are you sure? Y/N?")
        if (decision == 'Y'):
            to_be_deleted.directory.delete_element(to_be_deleted)
    else:
        to_be_deleted.directory.delete_element(to_be_deleted)
        # to za mało bo co jak ktos bedzie chciał zobaczyc plik?
        # a jak to sie ma do funkcji size?


def get_path(working_dir, home):
    path = '~/home'
    text = ''
    while working_dir != home:
        text = working_dir.name + '/' + text
        working_dir = working_dir.directory
    path = (path + '/' + text + ' ') if text != '' else (path + ' ')
    return path


def count(working_dir, folder):
    try:
        number = len(working_dir.find(folder).content)
    except AttributeError:
        pass
    return number


def cat(working_dir, request):
    """
    Prints file/folder info.
    """
    wanted_info = str(working_dir.find(request))
    print(wanted_info)
