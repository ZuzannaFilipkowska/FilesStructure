from structure import File, Folder
from main import cd

home = Folder('home')
working_dir = 'home'

plik1 = File(home, 'plik1', 'txt', 1)
plik2 = File(home, 'plik2', 'txt', 2)
folder1 = Folder('folder1', home)
plik3 = File(folder1, 'plik3', 'txt', 3)
answer = "cd folder1".split()
cd(answer, working_dir, home)

home.ls(answer[1])
pass
