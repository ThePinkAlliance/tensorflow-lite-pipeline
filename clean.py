import xml.etree.ElementTree as et
import os
import shutil

from pipeline import DATASET_DIR

files = os.listdir("./" + DATASET_DIR + "/annotation-2")

for f in files:
    if f.endswith("Jpg"):
        shutil.move("./" + DATASET_DIR + "/annotation-2/" + f.title(),
                    "./" + DATASET_DIR + "/trash/" + f.title())
