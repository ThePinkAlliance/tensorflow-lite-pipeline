import argparse
import os


print("\n \n \n=============================================")
print("MAKE SURE NO IMAGES ARE IN THE IMAGES FOLDER!")
print("=============================================\n \n \n")

parser = argparse.ArgumentParser()
parser.add_argument("--video", help="path for video", dest='vid')
parser.add_argument("--frame", help="frame per second",
                    dest='frames', default="10")
parser.add_argument("--dir-name", help="dir name for frames", dest="dir")
args = parser.parse_args()

vid_path = args.vid
dir = args.dir

images_dir_exist = os.path.isdir("./dataset/"+str(dir))

if images_dir_exist == False:
    os.mkdir("./dataset/"+str(dir)+"/")


if vid_path != None:
    os.system("ffmpeg -i " + vid_path +
              " -vf fps=" + str(args.frames) + " ./dataset/"+str(dir)+"/img%02d.jpg")
else:
    print("::> Please define --video flag")
