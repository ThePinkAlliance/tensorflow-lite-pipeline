import io
from typing import Iterable
import xml.etree.ElementTree as et
import os
import csv
from csv import DictWriter
import random
import shutil

trainExists = os.path.isfile("./dataset/train_labels.csv")
testExists = os.path.isfile("./dataset/test_labels.csv")

if trainExists == True and testExists == True:
    os.remove("./dataset/train_labels.csv")
    os.remove("./dataset/test_labels.csv")

files_train = os.listdir("./dataset/train")
files_test = os.listdir("./dataset/test")

test_labels_written = False
train_labels_written = False

# this segment of the script will randomize the images
image_paths = os.listdir('dataset/images')
random.shuffle(image_paths)


row_labels = (
    "filename", "height", "width",
    "label", "xmin", "ymin", "xmax", "ymax"
)

for i, image_path in enumerate(image_paths):
    print(image_path)

    if i < int(len(image_paths) * 0.8):
        shutil.copy(
            f'dataset/images/{image_path}', 'dataset/train')
        shutil.copy(
            f'dataset/annotations/{image_path.replace("jpg", "xml")}', 'dataset/train')
    else:
        shutil.copy(
            f'dataset/images/{image_path}', 'dataset/test')
        shutil.copy(
            f'dataset/annotations/{image_path.replace("jpg", "xml")}', 'dataset/test')

# start of the manifest creation script


def getData(file: str, path: str):
    x = et.parse(path + file.title())
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
        dat = getData(file, "./dataset/train/")
        file = open("./dataset/train_labels.csv", newline="", mode="a")
        writer = csv.writer(file, "excel")

        if train_labels_written == False:
            writer.writerow(row_labels)
            train_labels_written = True

        writer.writerow(dat)

for file in files_test:
    if (file.endswith("xml")):
        dat = getData(file, "./dataset/test/")
        file = open("./dataset/test_labels.csv", newline="", mode="a")
        writer = csv.writer(file, "excel")

        if test_labels_written == False:
            writer.writerow(row_labels)
            test_labels_written = True

        writer.writerow(dat)
