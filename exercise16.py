import os

dir_list = []
os.chdir('main')
for dirpath, dirnames, filenames in os.walk('main'):
    for file in filenames:
        if file.endswith(".py"):
            dir_list.append(dirpath.replace("\\", "/"))
            break

dir_list.sort()
with open('../new.txt', 'w') as f:
    f.write('\n'.join(dir_list))
