import io
import os
import shutil

from pipeline import ANNOTATIONS_DIRECTORY, DATASET_DIR, DIRS_INCLUDE_DATA, DIRS_INCLUDE_IMG, IMAGES_DIRECTORY, WORKING_DIR


def mix():
    # delete the annotations directory and create a new one
    if os.path.exists(ANNOTATIONS_DIRECTORY) == False:
        os.mkdir(ANNOTATIONS_DIRECTORY)

    # delete the images directory and create a new one
    if os.path.exists(IMAGES_DIRECTORY) == False:
        os.rmdir(IMAGES_DIRECTORY)
        os.mkdir(IMAGES_DIRECTORY)

    for dir in DIRS_INCLUDE_IMG:
        files = os.listdir(WORKING_DIR + "\\"+DATASET_DIR + "\\" + dir)
        for file in files:
            path = WORKING_DIR + "\\" + DATASET_DIR + "\\" + dir + "\\" + file

            newPath = IMAGES_DIRECTORY + "\\" + file

            shutil.copy(path, newPath)

    for dir in DIRS_INCLUDE_DATA:
        files = os.listdir(WORKING_DIR + "\\" + DATASET_DIR + "\\" + dir)
        for file in files:
            path = WORKING_DIR + "\\" + DATASET_DIR + "\\" + dir + "\\" + file

            newPath = ANNOTATIONS_DIRECTORY + "\\" + file

            shutil.copy(path, newPath)


mix()
