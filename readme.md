# Tensorflow Lite Pipeline

check `model_maker_object_detection.ipynb` for a in depth look at how the model is trained.

## Requirements

- CUDA Version 11.x [download](https://developer.nvidia.com/rdp/cudnn-download)
- cuDNN Version 8.1 [download](https://developer.nvidia.com/rdp/cudnn-archive)
- ffmpeg [download](https://community.chocolatey.org/packages/ffmpeg)
- Tensorflow 2.5.0
- Python 3.6 -> 3.9

### Create Virtual Enviroment

```powershell
python -m venv venv

# cd into the scripts directory
cd venv/Scripts

# activate the virtual enviroment
activate

# Change to the parent directory where all the scripts are
cd ..
```

### Install Dependencies

```powershell
pip install tensorflow==2.5.0
pip install --use-deprecated=legacy-resolver tflite_model_maker
pip install pycocotools
pip install numpy
pip install opencv-python
```

### Converting video into frames (Optional)

The video converter script has two flags `--video` to specify the video location
and `--frame` will tell ffmpeg how many frames it should generate per second three is a good median.

```ps
py convert.video.py --video ./dataset/videos/one.mp4 --dir-name images-2
```

### Mix data from the different folders of data

mixing the data will combine all the annotations and images listed in the config.json file into annotations and images folders for create-data.py to process.

```powershell
py dataset.mixer.py
```

### Create dataset

create-dataset.py will take all the files in the images and annotations folders and randomly copy them to the `test` and `train` folder's for tensorflow to use.

When making your own dataset use a minimum of 233 images for training to label data using [labelimg](https://github.com/tzutalin/labelImg) is a good choice.

```powershell
py create-dataset.py
```

### Train the model

Model training collects all the annotations and images and passes them to tensorflow to start training the object detection model.

```powershell
py new.py
```
