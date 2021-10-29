from src import DL_PATH
from os import path

def isPathValid(_path):
    if path.isdir(_path):
        return True
    else:
        return False