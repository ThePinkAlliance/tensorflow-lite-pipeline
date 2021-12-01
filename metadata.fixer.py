import xml.etree.ElementTree as et

import argparse
import os

imageNames = []

parser = argparse.ArgumentParser()

parser.add_argument("--dir-annotaion",
                    default="./annotation-2", dest="dirAnnotation")
parser.add_argument("--dir-image", default="./image-2", dest="dirImage")
parser.add_argument("--img-out", dest="imgout", default="./images")
parser.add_argument("--char", default="3", dest="char")

args = parser.parse_args()

dirAnnotations = args.dirAnnotation
dirImages = args.dirImage
dirImgOut = args.imgout
char = args.char

if os.path.exists(dirAnnotations) == False:
    os.mkdir(dirAnnotations)

filesAnnotation = os.listdir(dirAnnotations)

if os.path.exists(dirImages) == False:
    os.mkdir(dirImages)

filesImages = os.listdir(dirImages)

for image in filesImages:
    imageNames.append(image.title())

print(imageNames)

for i, filef in enumerate(filesAnnotation):

    imgName = imageNames[i]

    x = et.parse(dirAnnotations + "/" + filef.title())
    root = x.getroot()

    name = root[1]
    path = root[2]

    newPath = dirImgOut + "\\" + imgName

    name.text = imgName
    path.text = newPath

    x.write(dirAnnotations + "/" + filef.title())

print("=== FILE INFO FIXED! ===")
