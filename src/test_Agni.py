import numpy as np
from glob import glob

from skimage.transform import resize
from skimage import io

from keras.models import load_model
from keras import backend as K


# input image dimensions
img_rows, img_cols = 128, 128


data_path = '../data/'

def get_label(filename):
    if 'side' in filename.split('/')[-2]:
        return np.array([0, 1])
    else:
        return np.array([1, 0])

x_test_files = glob(data_path+'valid/*/*')
images_labels_test = [[np.float32(resize(io.imread(x, as_grey=True), (img_rows, img_cols))), get_label(x)] for x in x_test_files]

X_test, Y_test = map(np.array, zip(*images_labels_test))

# change ordering for theano
if K.image_dim_ordering() == 'th':
    X_test = X_test.reshape([-1, 1, img_rows, img_cols])
    input_shape = (1, img_rows, img_cols)
else:
    X_test = X_test.reshape([-1, img_rows, img_cols, 1])
    input_shape = (img_rows, img_cols, 1)


model = load_model("agni.hdf5")


score = model.evaluate(X_test, Y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
