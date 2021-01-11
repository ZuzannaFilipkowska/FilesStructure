from structure import Folder


def cd(answer, working_dir, home):
    """
    Returns new working directory.
    """
    if len(answer) == 1:
        # go to the home folder
        working_dir = home
        return working_dir
    elif len(answer) == 2:
        if answer[1] == "..":
            # move one directory up
            if working_dir is home:
                return working_dir
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


def rm(to_be_deleted, working_dir, home):
    """
    Removes given folder or file from working directory.
    """
    if to_be_deleted is not home:
        decision = input("Are you sure? Y/N? ")
        if (decision == 'Y'):
            to_be_deleted.directory.delete_element(to_be_deleted)
            return "Element was removed"
        else:
            return "Aborting"
    else:
        return "You can't remove home directory"


def get_path(working_dir, home):
    """
    Returns current path.
    """
    path = '~/home'
    text = ''
    while working_dir != home:
        text = working_dir.name + '/' + text
        working_dir = working_dir.directory
    path = (path + '/' + text + ' ') if text != '' else (path + ' ')
    return path


def wc(working_dir, request):
    if len(request) == 2:
        return working_dir.find(request[1]).count_elements()
    elif len(request) == 3:
        if request[1] == '-f':
            file_number = working_dir.find(request[2]).count_only_files()
            return file_number
        elif request[1] == '-r':
            elements_number = 0
            elements_number = working_dir.find(request[2]).count_elements_recursive()
            return elements_number
    elif len(request) == 4:
        if request[1] == '-r' and request[2] == '-f':
            size = working_dir.find(request[3]).count_files_recursive()
            return size
        elif request[1] == '-f' and request[2] == '-r':
            size = working_dir.find(request[3]).count_files_recursive()
            return size


def count_elements_recursive(folder, size):
    size += folder.count_elements()
    for element in folder:
        if isinstance(element, Folder):
            size += count_elements_recursive(element)  # czy bez size =
    return size


def cat(working_dir, request):
    """
    Prints file/folder info.
    """
    wanted_info = str(working_dir.find(request))
    print(wanted_info)


def ls(working_dir, request):
    # name = working_dir.name if (len(request) == 0) else request[1]
    if len(request) == 1:
        name = working_dir.name
    else:
        name = request[1]
    if working_dir.name == name:
        return working_dir.list_elements()
    for element in working_dir.content:
        if isinstance(element, Folder):
            if element.name == name:
                return element.list_elements()  # czy ten return jest ok?
    print(f"ls: cannot access {name}: No such file or directory")


def cp_mv(working_dir, request, home, delete_original):
    if len(request) == 4:
        if request[1][0] == "/":
            original = working_dir.find(request[1])
            # rozszyfruj sciezke drugiego /home/folder1 nazwa
            path = request[2].split('/')[1:]
            destination = home  # czy to hoem nie bedzie zmienione?
            for i in range(0, len(path)-1):
                destination = destination.find(path[i+1])
            # przekopiuj
            copy_name = request[3]
            original.copy(destination, copy_name)
            if(delete_original):
                original.directory.delete_element(original)
        else:
            original = working_dir.find(request[1])
            destination = working_dir.find(request[2])
            copy_name = request[3]
            original.copy(destination, copy_name)
            if(delete_original):
                original.directory.delete_element(original)
    elif len(request) == 3:
        # creates copy in working dir
        copy_name = request[2]
        original = working_dir.find(request[1])
        original.copy(working_dir, copy_name)
        if(delete_original):
            original.directory.delete_element(original)


"""
jeszcze komenda --help
taka co wyswietla mozliwe komendy
"""