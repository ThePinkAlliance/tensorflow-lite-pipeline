# Tensorflow Lite Pipeline

check `model_maker_object_detection.ipynb` for in depth look at how the model is trained.

### Requirements

- CUDA Version 11.x [download](https://developer.nvidia.com/rdp/cudnn-download)
- cuDNN Version 8.1 [download](https://developer.nvidia.com/rdp/cudnn-archive)
- ffmpeg [download](https://community.chocolatey.org/packages/ffmpeg)
- Tensorflow 2.5.0
- Python 3.6 -> 3.9

#### Create Virtual Enviroment

```powershell
python -m venv venv
```

#### Install Dependencies

```powershell
pip install tensorflow==2.5.0
pip install --use-deprecated=legacy-resolver tflite_model_maker
pip install pycocotools
pip install numpy
pip install opencv-python
```

#### Converting video into frames

The video converter script has two flags `--video` to specify the video location
and `--frame` will tell ffmpeg how many frames it should generate per second three is a good median.

```ps
python convert.video.py --video ./dataset/videos/one.mp4 --dir-name images-2
```

#### Create dataset

When making your own dataset use a minimum of 233 images for training
for image labeling [labelimg](https://github.com/tzutalin/labelImg) is a good option.

```powershell
# cd into the scripts directory
cd venv/Scripts

# activate the virtual enviroment
activate

# run create-dataset script
python create-dataset.py
```

#### Train the model

Training does take an average of **10 -> 20mins depending on your machine**

```powershell
# train the tensorflow lite model
python new.py
```
