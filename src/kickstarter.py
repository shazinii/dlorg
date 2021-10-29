from src import DL_PATH
from src.path_validation import isPathValid
from os import listdir, path

#Get Only Files from Download Folder
def getFileProp():
    if isPathValid(DL_PATH):
        DL_FOLDER_ITEMS = listdir(DL_PATH)
        filtered_files = []
        if len(DL_FOLDER_ITEMS) >0:
            for idx, itm in enumerate(DL_FOLDER_ITEMS):
                if path.isfile(path.join(DL_PATH, itm)):
                    _file_prop_dict = {
                        "name": itm.split(".")[0],
                        "extension": itm.split(".")[-1],
                        "path": path.join(DL_PATH, itm)
                    }
                    filtered_files.append(_file_prop_dict)

    return filtered_files

