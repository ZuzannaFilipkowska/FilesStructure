from structure import Folder


def cd(answer, working_dir, home):
    if answer[1] == "..":
        # wróć do folderu wyżej
        working_dir = working_dir.directory
        return working_dir
    elif answer[1] == '.':
        # wroc do folderu glownego
        working_dir = home
        return working_dir
    else:
        # wejdz do podanego folderu
        given_folder = answer[1]
        if given_folder[0] == '/':
            given_folder = given_folder[1:]
            working_dir = home.find(given_folder)
            return working_dir
        else:
            working_dir = working_dir.find(given_folder)
            return working_dir


def rm(answer, working_dir, home):
    """
    Removes given folder or file.
    """
    to_be_deleted = home.find(answer[1])
    if isinstance(to_be_deleted, Folder):
        decision = input(f"Are you sure you want to delete {answer[1]} folder? Y/N?")
        if (decision == 'Y'):
            to_be_deleted.directory.content.remove(self)
    else:
        to_be_deleted.directory.content.remove(self)
        # to za mało bo co jak ktos bedzie chciał zobaczyc plik?
        # a jak to sie ma do funkcji size?


def get_path():
    pass
