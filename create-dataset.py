import io
from typing import Iterable
import xml.etree.ElementTree as et
import os
import csv
import random
import shutil

trainExists = os.path.isfile("./dataset/train_labels.csv")
testExists = os.path.isfile("./dataset/test_labels.csv")

if trainExists == True and testExists == True:
    os.remove("./dataset/train_labels.csv")
    os.remove("./dataset/test_labels.csv")

files_train = os.listdir("./dataset/train")
files_test = os.listdir("./dataset/test")

names: list[str] = []
xmins: list[str] = []
ymins: list[str] = []
xmaxs: list[str] = []
ymaxs: list[str] = []
heights: list[str] = []
widths: list[str] = []
labels: list[str] = []

# this segment of the script will randomize the images
image_paths = os.listdir('dataset/images')
random.shuffle(image_paths)


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


def writeManifest(path: str, data: Iterable):
    file = open(path, newline="", mode="a")

    writer = csv.writer(file, "excel")

    writer.writerow(data)


for file in files_train:
    if (file.endswith("xml")):
        dat = getData(file, "./dataset/train/")
        writeManifest("./dataset/train_labels.csv", dat)

for file in files_test:
    if (file.endswith("xml")):
        dat = getData(file, "./dataset/test/")
        writeManifest("./dataset/test_labels.csv", dat)
