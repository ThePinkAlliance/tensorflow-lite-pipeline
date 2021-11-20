import xml.etree.ElementTree as et
import os
import shutil

files = os.listdir("./dataset/raw")

for f in files:
    if f.endswith("xml"):
        shutil.move("./dataset/raw/" + f.title(),
                    "./dataset/annotations/" + f.title())
