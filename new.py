import tensorflow as tf
from tensorflow_examples.lite.model_maker.core.data_util.object_detector_dataloader import DetectorDataLoader
from tensorflow_examples.lite.model_maker.core.task.model_spec import IMAGE_CLASSIFICATION_MODELS

from tflite_model_maker import object_detector
from tflite_model_maker import model_spec

from absl import logging
import numpy as np


assert tf.__version__.startswith('2')


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
