from structure import Folder, File


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
            if "/" in given_folder:
                path = given_folder.split('/')
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
        text = '/' + working_dir.name + text
        working_dir = working_dir.directory
    path = (path + text + ' ') if text != '' else (path + ' ')
    return path


def wc(working_dir, request):
    """
    Returns number of elements in a folder,
    counts recursively or counts just files if requested.
    """
    if len(request) == 2:
        return working_dir.find(request[1]).count_elements()
    elif len(request) == 3:
        if request[1] == '-f':
            num_of_files = working_dir.find(request[2]).count_only_files()
            return num_of_files
        elif request[1] == '-r':
            folder = working_dir.find(request[2])
            num_of_files = folder.count_elements_recursive()
            return num_of_files
    elif len(request) == 4:
        if request[1] == '-r' and request[2] == '-f':
            folder = working_dir.find(request[3])
            num_of_files = folder.count_only_files_recursive()
            return num_of_files
        elif request[1] == '-f' and request[2] == '-r':
            folder = working_dir.find(request[3])
            num_of_files = folder.count_only_files_recursive()
            return num_of_files


def cat(working_dir, element_name):
    """
    Returns file/folder info.
    """
    wanted_info = str(working_dir.find(element_name))
    if wanted_info is not None:
        return wanted_info
    else:
        return f"{element_name}: No such file or directory"


def ls(working_dir, request):
    name = working_dir.name if (len(request) == 1) else request[1]
    element = working_dir.find(name)
    try:
        if isinstance(element, File):
            return element.name
        elif isinstance(element, Folder):
            return element.list_elements()
        return (f"ls: cannot access {name}: No such file or directory")
    except Exception:
        return(f"ls: cannot access {name}: No such file or directory")


def cp(working_dir, request, home):
    if len(request) == 4:
        # creates copy in given directory
        if "/" in request[2]:
            original = working_dir.find(request[1])
            path = request[2].split('/')
            destination = home  # czy to home nie bedzie zmienione?
            for i in range(0, len(path)-1):
                destination = destination.find(path[i+1])
            copy_name = request[3]
            original.copy(destination, copy_name)
        else:
            original = working_dir.find(request[1])
            destination = working_dir.find(request[2])
            copy_name = request[3]
            original.copy(destination, copy_name)
    elif len(request) == 3:
        # creates copy in working dir
        copy_name = request[2]
        original = working_dir.find(request[1])
        original.copy(working_dir, copy_name)


def mv(working_dir, request, home):
    cp(working_dir, request, home)
    original = working_dir.find(request[1])
    original.directory.delete_element(original)


def help():
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
    return manual
