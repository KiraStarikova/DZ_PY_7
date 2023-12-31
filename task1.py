import pathlib

file_name = 'renamed'
num = 4
ex_old = 'xml'
ex_new = 'txt'

def renameFiles (file_name, num, ex_old, ex_new):
    p = pathlib.Path('dir/')
    my_list = []
    for i in p.iterdir():
        my_list.append(i.name)
    count = 1
    for i in range(len(my_list)):
        temp = my_list[i].split('.')
        if temp[1] == ex_old:
            new_name = file_name + funcCount(count, num) + '.' + ex_new
            old = pathlib.Path('dir/' + temp[0] + '.' + ex_old)
            old.rename('dir/' + new_name)
            count += 1


def funcCount (count, num):
    s = str(count)
    for i in range(num):
        s = str(0) + s
    if len(s) > num:
        s = s[len(s) - num:]
    return s




renameFiles (file_name, num, ex_old, ex_new)