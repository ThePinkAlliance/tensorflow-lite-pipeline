import tensorflow as tf
from tensorflow_examples.lite.model_maker.core.data_util.object_detector_dataloader import DetectorDataLoader

from tflite_model_maker import object_detector
from tflite_model_maker import model_spec

from absl import logging
import numpy as np


assert tf.__version__.startswith('2')


def create_image_result():
    INPUT_IMAGE_URL = "https://storage.googleapis.com/cloud-ml-data/img/openimage/3/2520/3916261642_0a504acd60_o.jpg"
    DETECTION_THRESHOLD = 0.3

    TEMP_FILE = '/tmp/image.png'

    im = Image.open(TEMP_FILE)
    im.thumbnail((512, 512), Image.ANTIALIAS)
    im.save(TEMP_FILE, 'PNG')

    # Load the TFLite model
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()

    # Run inference and draw detection result on the local copy of the original file
    detection_result_image = run_odt_and_draw_results(
        TEMP_FILE,
        interpreter,
        threshold=DETECTION_THRESHOLD
    )

    # Show the detection result
    Image.fromarray(detection_result_image)


tf.get_logger().setLevel('ERROR')
logging.set_verbosity(logging.ERROR)

spec = model_spec.get('efficientdet_lite0')

test_data: DetectorDataLoader = object_detector.DataLoader.from_pascal_voc(
    "./dataset/test", "./dataset/test", label_map={1: "me"})

train_data: DetectorDataLoader = object_detector.DataLoader.from_pascal_voc(
    "./dataset/train", "./dataset/train", label_map={1: "me"})

model = object_detector.create(train_data, model_spec=spec, batch_size=8,
                               train_whole_model=True, validation_data=test_data)

model.evaluate(test_data)

model.export(export_dir='.')
model.evaluate_tflite('model.tflite', test_data)

create_image_result()
