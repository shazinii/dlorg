from os import listdir, environ, path
_path = environ.get("HOME")
_dir_items = listdir(_path)
_dir_files=[]
for idx, itm in enumerate(_dir_items):
    if path.isfile(path.join(_path, itm)):
        _dir_files.append(path.join(_path, itm))

#Readable

for i in _dir_files:
    print(i)