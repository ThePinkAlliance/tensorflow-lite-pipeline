import xml.etree.ElementTree as et
import os
import csv
import shutil
import random

from pipeline import ANNOTATIONS_DIRECTORY, DATASET_DIR, IMAGES_DIRECTORY, TESTING_DIRECTORY, TRAINING_DIRECTORY

trainExists = os.path.isfile("./" + DATASET_DIR + "/train_labels.csv")
testExists = os.path.isfile("./" + DATASET_DIR + "/test_labels.csv")

trainDirExists = os.path.isdir(TRAINING_DIRECTORY)
testDirExists = os.path.isdir(TESTING_DIRECTORY)

if trainExists == True and testExists == True:
    os.remove("./" + DATASET_DIR + "/train_labels.csv")
    os.remove("./" + DATASET_DIR + "/test_labels.csv")

if trainDirExists == False and testDirExists == False:
    os.mkdir(TRAINING_DIRECTORY)
    os.mkdir(TESTING_DIRECTORY)

files_train = os.listdir(TRAINING_DIRECTORY)
files_test = os.listdir(TESTING_DIRECTORY)

test_labels_written = False
train_labels_written = False

# this segment of the script will randomize the images
image_paths = os.listdir(IMAGES_DIRECTORY)
random.shuffle(image_paths)


row_labels = (
    "filename", "height", "width",
    "class", "xmin", "ymin", "xmax", "ymax"
)

for i, image_path in enumerate(image_paths):
    print(image_path)

    if i < int(len(image_paths) * 0.8):
        shutil.copy(
            f'' + IMAGES_DIRECTORY + "\\" + image_path + '', '' + DATASET_DIR + '/train')
        shutil.copy(
            f'' + ANNOTATIONS_DIRECTORY + "\\" + image_path.replace("jpg", "xml") + '', '' + DATASET_DIR + '/train')
    else:
        shutil.copy(
            f'' + IMAGES_DIRECTORY + "\\" + image_path + '', '' + DATASET_DIR + '/test')
        shutil.copy(
            f'' + ANNOTATIONS_DIRECTORY + "\\" + image_path.replace("jpg", "xml") + '', '' + DATASET_DIR + '/test')

# start of the manifest creation script


def getData(file: str, path: str):
    x = et.parse(path + "\\" + file.title())
    root = x.getroot()

    name = root[1].text

    height = root[4][0].text
    width = root[4][1].text

    label = root[6][0].text

    xmin = root[6][4][0].text
    ymin = root[6][4][1].text
    xmax = root[6][4][2].text
    ymax = root[6][4][3].text

    return name, height, width, label, xmin, ymin, xmax, ymax


for file in files_train:
    if (file.endswith("xml")):
        dat = getData(file, TRAINING_DIRECTORY)
        file = open("./" + DATASET_DIR + "/train_labels.csv",
                    newline="", mode="a")
        writer = csv.writer(file, "excel")

        if train_labels_written == False:
            writer.writerow(row_labels)
            train_labels_written = True

        writer.writerow(dat)

for file in files_test:
    if (file.endswith("xml")):
        dat = getData(file, TESTING_DIRECTORY)
        file = open("./" + DATASET_DIR + "/test_labels.csv",
                    newline="", mode="a")
        writer = csv.writer(file, "excel")

        if test_labels_written == False:
            writer.writerow(row_labels)
            test_labels_written = True

        writer.writerow(dat)
