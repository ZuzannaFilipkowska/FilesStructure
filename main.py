from structure import File, Folder
from commands import cd, rm, get_path, cat, ls, wc, cp_mv


def main():
    home = Folder('home')
    working_dir = Folder('working_dir')
    working_dir = home
    answer = True

    while answer:
        try:
            path = get_path(working_dir, home)

            answer = input(path).split()

            if answer[0] == "cd":
                new_working_dir = cd(answer, working_dir, home)
                if new_working_dir:
                    working_dir = new_working_dir
                else:
                    print("Incorrect usage of: cd. Try again")
            elif answer[0] == 'mkdir':
                # make folder
                try:
                    Folder(answer[1], working_dir)
                except Exception:
                    print("Incorrect usage of: mkdir. Try again")
            elif answer[0] == 'mk':
                # make file
                try:
                    File(working_dir, answer[1], answer[2], answer[3])
                except Exception:
                    print("Incorrect usage of: mk. Try again")
            elif answer[0] == 'rm':
                # delete file or folder
                if len(answer) == 2:
                    to_be_deleted = working_dir.find(answer[1])
                    if to_be_deleted:
                        print(rm(to_be_deleted, working_dir, home))
                    else:
                        print(f"Error. {answer[1]} - Element does not exist")
                else:
                    print("Incorrect usage of: rm. Try again")
            elif answer[0] == 'ls':
                # print structure
                try:
                    ls(working_dir, answer)
                except Exception:
                    print("Incorrect usage of: ls. Try again")
            elif answer[0] == 'cat':
                # print file/folder info
                cat(answer[1])
            elif answer[0] == 'size':
                # print folder size
                size = working_dir.find(answer[1]).count_size_recursive()
                print(f'Size: {size} B')
            elif answer[0] == 'wc':
                # count elements in folder
                print(wc(working_dir, answer))
            elif answer[0] == 'pwd':
                print(working_dir.name)
            elif answer[0] == 'cp':
                cp_mv(working_dir, answer, home, False)
            elif answer[0] == 'mv':
                cp_mv(working_dir, answer, home, True)
            elif answer[0] == 'exit':
                # end program
                answer = False
            else:
                print("Command not found")
        except IndexError:
            print("No command was given. Try again.")
            main()


if __name__ == "__main__":
    main()
