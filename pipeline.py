import os
import sys
import io
import xml.etree.ElementTree as et
import json


if sys.argv[0] == "pipeline.py":
    print("DONT RUN ME FROM THE TERMINAL")
    exit()


WORKING_DIR = os.getcwd()
CONFIG = None

with open("./config.json", "r") as config_file:
    CONFIG = json.load(config_file)
    config_file.close()


print("Current Config: " + str(CONFIG))

DATASET_DIR = CONFIG["dataset-dir"] or "dataset"

TRAINING_DIRECTORY = WORKING_DIR + "\\"+DATASET_DIR+"\\train"
TESTING_DIRECTORY = WORKING_DIR + "\\"+DATASET_DIR+"\\test"

IMAGES_DIRECTORY = WORKING_DIR + "\\"+DATASET_DIR+"\\" + CONFIG["image-dir"]
ANNOTATIONS_DIRECTORY = WORKING_DIR + "\\" + \
    DATASET_DIR+"\\" + CONFIG["annotation-dir"]

DO_IMAGES_EXIST = os.path.exists(IMAGES_DIRECTORY)
DO_ANNOTATIONS_EXIST = os.path.exists(ANNOTATIONS_DIRECTORY)

if DO_IMAGES_EXIST == False:
    os.mkdir(IMAGES_DIRECTORY)

if DO_ANNOTATIONS_EXIST == False:
    os.mkdir(ANNOTATIONS_DIRECTORY)

# list of labels in dataset
LABEL_MAP = {}

# populate the label map dict with data from the config file
for label in CONFIG["label_map"]:
    LABEL_MAP.update({1: label})

DIRS_INCLUDE_IMG = CONFIG["images"]
DIRS_INCLUDE_DATA = CONFIG["annotations"]

MODEL_TYPE = CONFIG["model-type"] or "efficientdet_lite0"
EXPORT_PATH = CONFIG["export-path"] or "model.tflite"

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
        files = os.listdir("./" + DATASET_DIR + "/" + _img)
        IMAGES[_img] = files

    for _img in DIRS_INCLUDE_DATA:
        files = os.listdir("./" + DATASET_DIR + "/" + _img)
        ANNOTATION[_img] = files

    print(ANNOTATION.keys())

    keys = ANNOTATION.keys()
    missingFiles = len(ANNOTATIONS_MISSING) > 0

    # make this run for all the folders in the ANNOTATION object
    for _key in keys:
        for _ann in ANNOTATION[_key]:
            isFileMissing("./" + DATASET_DIR + "/" + _key + "/" + _ann)

    return missingFiles
