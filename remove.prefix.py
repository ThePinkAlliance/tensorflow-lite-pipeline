import os

dir = "C:\\Users\\capts\\Desktop\\code\\python\\vision\dataset\\annotation-2"

target_prefix = "33"

files = os.listdir(dir)


def addNameToPath(name: str) -> str:
    return dir + "\\" + name


for file in files:
    newName = file.removeprefix(target_prefix)

    os.rename(addNameToPath(file), addNameToPath(newName))
