from structure import File, Folder
from functions import cd


def main():
    home = Folder('home')
    working_dir = Folder('working_dir')
    working_dir = home
    # teraz working_dir jest też folderem
    answer = True
    while answer:
        # path = '~/home'
        # print(path)
        print("Waiting for command: ")
        answer = input().split()
        if answer[0] == "cd":
            working_dir = cd(answer, working_dir, home)
        elif answer[0] == 'mkdir':
            # make folder
            Folder(answer[1], working_dir)
        elif answer[0] == 'mk':
            # make file
            File(working_dir, answer[1], answer[2], answer[3])
        elif answer[0] == 'rm':
            # delete file
            pass
        elif answer[0] == 'rmdir':
            # delete folder
            pass
        elif answer[0] == 'ls':
            # print structure
            working_dir.list_elements()
        elif answer[0] == 'cat':
            # print file/folder info
            pass
        elif answer[0] == 'size':
            # print folder size
            pass
        elif answer[0] == 'exit':
            # end program
            answer = False


if __name__ == "__main__":
    main()
