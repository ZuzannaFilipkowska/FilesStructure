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


def get_path():
    pass
