from __future__ import print_function
import numpy as np
from skimage import io
from skimage.transform import resize
from itertools import product
import random
import os
from glob import glob

# for reproducibility
np.random.seed(42)

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import normalization
from keras.utils import np_utils
from keras.preprocessing.image import ImageDataGenerator
from keras import backend as K
from keras import optimizers
from keras.callbacks import TensorBoard

# input image dimensions
img_rows, img_cols = 128, 128


data_path = '../data/'

def get_label(filename):
    if 'side' in filename.split('/')[-2]:
        return np.array([0, 1])
    else:
        return np.array([1, 0])

x_train_file_names = glob(data_path+'train/*/*')
images_labels_train = [[np.float32(resize(io.imread(x, as_grey=True), (img_rows, img_cols))), get_label(x)] for x in x_train_file_names]
x_test_files = glob(data_path+'valid/*/*')
images_labels_test = [[np.float32(resize(io.imread(x, as_grey=True), (img_rows, img_cols))), get_label(x)] for x in x_test_files]


X_train, Y_train = map(np.array, zip(*images_labels_train))
X_test, Y_test = map(np.array, zip(*images_labels_test))

normal_count_train = 0
for test in Y_train:
    if np.array_equal(test, np.array([0, 1])):
        normal_count_train += 1

normal_count_test = 0
for test in Y_test:
    if np.array_equal(test, np.array([0, 1])):
        normal_count_test += 1

print('Train split: {0} (L), {1} (F)'.format(normal_count_train, len(Y_train)-normal_count_train))
print('Test split: {0} (L), {1} (F)'.format(normal_count_test, len(Y_test)-normal_count_test))

# change ordering for theano
if K.image_dim_ordering() == 'th':
    X_train = X_train.reshape([-1, 1, img_rows, img_cols])
    X_test = X_test.reshape([-1, 1, img_rows, img_cols])
    input_shape = (1, img_rows, img_cols)
else:
    X_train = X_train.reshape([-1, img_rows, img_cols, 1])
    X_test = X_test.reshape([-1, img_rows, img_cols, 1])
    input_shape = (img_rows, img_cols, 1)


print('X_train shape:', X_train.shape)
print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')


batch_size = 16
nb_classes = 2
nb_epoch = 100

# number of convolutional filters to use
nb_filters = 32
# size of pooling area for max pooling
pool_size = (4, 4)
# convolution kernel size
kernel_size = (3, 3)


model = Sequential()
model.add(normalization.BatchNormalization(input_shape=input_shape))
model.add(Convolution2D(32, kernel_size[0], kernel_size[1],
                        border_mode='valid'))
model.add(Activation('relu'))
model.add(Convolution2D(32, kernel_size[0], kernel_size[1],
                        border_mode='valid'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=pool_size))

model.add(normalization.BatchNormalization())
model.add(Convolution2D(64, kernel_size[0], kernel_size[1],
                        border_mode='valid'))
model.add(Activation('relu'))
model.add(Convolution2D(64, kernel_size[0], kernel_size[1],
                        border_mode='valid'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=pool_size))

model.add(Flatten())
model.add(Dense(256))
model.add(Activation('relu'))
# model.add(Dropout(0.5))
model.add(Dense(nb_classes))
model.add(Activation('softmax'))

adam = optimizers.Adam(lr=4e-06)
model.compile(loss='binary_crossentropy',
              optimizer=adam,
              metrics=['accuracy'])


datagen = ImageDataGenerator(
    rotation_range=5,  # randomly rotate images in the range (degrees, 0 to 180)
    width_shift_range=0.05,  # randomly shift images horizontally (fraction of total width)
    height_shift_range=0.05,  # randomly shift images vertically (fraction of total height)
    horizontal_flip=True,  # randomly flip images
    vertical_flip=False)  # randomly flip images

datagen.fit(X_train)


tb = TensorBoard(log_dir='./logs', histogram_freq=0, write_graph=True, write_images=False)

model.fit_generator(datagen.flow(X_train, Y_train,
                    batch_size=batch_size),
                    samples_per_epoch=X_train.shape[0],
                    nb_epoch=nb_epoch,
                    validation_data=(X_test, Y_test),
                    callbacks=[tb])


model.save("agni.hdf5")
