import argparse
import os

images_dir_exist = os.path.isdir("./dataset/images")

if images_dir_exist == False:
    os.mkdir("./dataset/images/")

print("\n \n \n=============================================")
print("MAKE SURE NO IMAGES ARE IN THE IMAGES FOLDER!")
print("=============================================\n \n \n")

parser = argparse.ArgumentParser()
parser.add_argument("--video", help="path for video", dest='vid')
args = parser.parse_args()

vid_path = args.vid

if vid_path != None:
    os.system("ffmpeg -i " + vid_path +
              " -vf fps=10 ./dataset/images/img%02d.jpg")
else:
    print("::> sPlease define --video flag")