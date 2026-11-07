import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import graphviz
import numpy as np
import scipy
import sklearn
import pandas as pd
import keras
import tensorflow as tf

print("Graphviz:", graphviz.__version__)
print("NumPy:", np.__version__)
print("SciPy:", scipy.__version__)
print("Scikit-learn:", sklearn.__version__)
print("Pandas:", pd.__version__)
print("Keras:", keras.__version__)
print("TensorFlow:", tf.__version__)