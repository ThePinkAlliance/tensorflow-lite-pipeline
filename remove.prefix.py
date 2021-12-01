import os

dir = "C:\\Users\\capts\\Desktop\\code\\python\\vision\dataset\\annotation-2"

files = os.listdir(dir)


def addNameToPath(name: str) -> str:
    return dir + "\\" + name


for file in files:
    newName = file.removeprefix("33")

    os.rename(addNameToPath(file), addNameToPath(newName))
