import os
import sys
import xml.etree.ElementTree as et


if sys.argv[0] == "pipeline.py":
    print("DONT RUN ME FROM THE TERMINAL")
    exit()


WORKING_DIR = os.getcwd()

TRAINING_DIRECTORY = WORKING_DIR + "\\dataset\\train"
TESTING_DIRECTORY = WORKING_DIR + "\\dataset\\test"

IMAGES_DIRECTORY = WORKING_DIR + "\\dataset\\images"
ANNOTATIONS_DIRECTORY = WORKING_DIR + "\\dataset\\annotations"

DO_IMAGES_EXIST = os.path.exists(IMAGES_DIRECTORY)
DO_ANNOTATIONS_EXIST = os.path.exists(ANNOTATIONS_DIRECTORY)

if DO_IMAGES_EXIST == False:
    os.mkdir(IMAGES_DIRECTORY)

if DO_ANNOTATIONS_EXIST == False:
    os.mkdir(ANNOTATIONS_DIRECTORY)

# list of labels in dataset
LABEL_MAP = {
    1: "red_shipping"
}

DIRS_INCLUDE_IMG = ["images-1", "images-2", "images-3"]
DIRS_INCLUDE_DATA = ["annotation-1", "annotation-2", "annotation-3"]

IMAGES = {}
ANNOTATION = {}

ANNOTATIONS_MISSING: list[str] = []


def isFileMissing(ann_dir: str):
    ann_name = ann_dir.split("/")[3]

    exists = os.path.exists(ann_dir)

    if exists:
        print("[ \u001b[32m✓\u001b[0m ] " + ann_name)

        x = et.parse(ann_dir)
        root = x.getroot()

        name = str(root[1].text)
        path = str(root[2].text)

        exists = os.path.exists(path)

        if exists:
            print("[ \u001b[32m✓\u001b[0m ] " + name)
        else:
            ANNOTATIONS_MISSING.append(name)
            print("[ \u001b[31m✖\u001b[0m ] " + name)
    else:
        ANNOTATIONS_MISSING.append(ann_name)
        print("[ \u001b[31m✖\u001b[0m ] " + ann_name)


def verifyIntegerty() -> bool:
    for _img in DIRS_INCLUDE_IMG:
        files = os.listdir("./dataset/" + _img)
        IMAGES[_img] = files

    for _img in DIRS_INCLUDE_DATA:
        files = os.listdir("./dataset/" + _img)
        ANNOTATION[_img] = files

    print(ANNOTATION.keys())

    keys = ANNOTATION.keys()
    missingFiles = len(ANNOTATIONS_MISSING) == 0

    # make this run for all the folders in the ANNOTATION object
    for _key in keys:
        for _ann in ANNOTATION[_key]:
            isFileMissing("./dataset/annotation-1/" + _ann)

    return missingFiles
