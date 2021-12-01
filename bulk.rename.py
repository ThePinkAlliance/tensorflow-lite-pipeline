import xml.etree.ElementTree as et
import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument("--dir", default="./images-1", dest="dir")
parser.add_argument("--char", default="3", dest="char")
parser.add_argument("--fix", dest="fix", type=bool)

args = parser.parse_args()

dir = args.dir
fix = args.fix
char = args.char

if os.path.exists(dir) == False:
    os.mkdir(dir)

files = os.listdir(dir)

for filef in files:
    location = dir + "/" + filef
    locationNew = dir + "/" + char + filef
    os.rename(location, locationNew)

print("=== DONE! ===")
