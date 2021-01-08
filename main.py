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
                    working_dir =  new_working_dir
                else:
                    print("Incorrect command. Try again")
            elif answer[0] == 'mkdir':
                # make folder
                Folder(answer[1], working_dir)
            elif answer[0] == 'mk':
                # make file
                File(working_dir, answer[1], answer[2], answer[3])
            elif answer[0] == 'rm':
                # delete file or folder
                rm(answer[1], working_dir)
            elif answer[0] == 'ls':
                # print structure
                ls(working_dir, answer)
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
        except IndexError:
            print("No command was given. Try again.")
            answer = input(path).split()


if __name__ == "__main__":
    main()
