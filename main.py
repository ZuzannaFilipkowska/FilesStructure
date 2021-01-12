from structure import File, Folder
from commands import cd, rm, get_path, cat, ls, wc, cp, mv, help


def main():
    home = Folder('home')
    working_dir = Folder('working_dir')
    working_dir = home
    answer = True
    starting_msg = "File system is working. Type help if needed or exit to end program./n"
    print(starting_msg)
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
                ls(working_dir, answer)
            elif answer[0] == 'cat':
                # print file/folder info
                print(cat(working_dir, answer[1]))
            elif answer[0] == 'size':
                # print folder size
                try:
                    size = working_dir.find(answer[1]).count_size_recursive()
                    print(f'Size: {size} kB')
                except AttributeError:
                    print("Incorrect usage of: size. Try again")
            elif answer[0] == 'wc':
                # count elements in folder
                try:
                    print(wc(working_dir, answer))
                except Exception:
                    print("Incorrect usage of: wc. Try again")
            elif answer[0] == 'pwd':
                print(working_dir.name)
            elif answer[0] == 'cp':
                try:
                    cp(working_dir, answer, home)
                except Exception:
                    print("Incorrect usage of: cp. Try again")
            elif answer[0] == 'mv':
                try:
                    mv(working_dir, answer, home)
                except Exception:
                    print("Incorrect usage of: mv. Try again")
            elif answer[0] == 'help':
                print(help())
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
