# Tensorflow Lite Pipeline

if you get lost at any point check `model_maker_object_detection.ipynb` for instructions.

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
```

#### Converting video into frames

```powershell
python convert.video.py --video ./dataset/videos/one.mp4
```

#### Create dataset

```powershell
# cd into the scripts directory
cd venv/Scripts

# activate the virtual enviroment
activate

# run create-dataset script
python create-dataset.py
```

#### Train the model

```powershell
# train the tensorflow lite model
python new.py
```
