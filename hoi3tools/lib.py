import os


def find(name, path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.find(name) != -1 and file.find("~") != 0:
                return os.path.join(root, file)
