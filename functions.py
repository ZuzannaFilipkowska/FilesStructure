def cd(answer, working_dir, home):
    if answer[0] == "cd":
        if answer[1] == "..":
            # wróć do folderu wyżej
            working_dir = home.find(working_dir).directory.name  # ok?
            return working_dir
        elif answer[1] == '.':
            # wroc do folderu glownego
            working_dir = home.name
            return working_dir
        else:
            # wejdz do podanego folderu
            given_folder = answer[1]
            if given_folder[0] == '/':
                working_dir = given_folder[1:]
                return working_dir
            else:
                working_dir = given_folder
                return given_folder

get_path():
    pass