import xml.etree.ElementTree as et
import os
import shutil

files = os.listdir("./dataset/annotation-2")

for f in files:
    if f.endswith("Jpg"):
        shutil.move("./dataset/annotation-2/" + f.title(),
                    "./dataset/trash/" + f.title())
