from structure import File, Folder


def cd(answer, working_dir, home):
    if answer[0] == "cd":
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
                home.look_for_folder(given_folder[1:], working_dir)
                return working_dir
            else:
                for element in working_dir.content:
                    if element.name == given_folder:
                        working_dir = None
                        working_dir = element
                        return working_dir


# def main():
#     home = Folder('home')
#     home.directory = home
#     working_dir = home
#     answer = True
#     while answer:
#         print("Waiting for command: ")
#         answer = input().split()
#         if answer[0] == "cd":
#             cd(answer, working_dir, home)
#         elif answer[0] == 'mkdir':
#             # make folder
#             Folder(answer[1], working_dir)
#         elif answer[0] == 'mk':
#             # make file
#             File(working_dir, answer[1], answer[2], answer[3])
#         elif answer[0] == 'rm':
#             # delete file
#             pass
#         elif answer[0] == 'rmdir':
#             # delete folder
#             pass
#         elif answer[0] == 'ls':
#             # print structure
#             working_dir.list_elements()
#         elif answer[0] == 'cat':
#             # print file/folder info
#             pass
#         elif answer[0] == 'size':
#             # print folder size
#             pass
#         elif answer[0] == 'exit':
#             # end program
#             answer = False


#main()
