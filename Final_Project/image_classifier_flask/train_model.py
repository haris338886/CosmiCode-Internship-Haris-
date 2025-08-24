import os
import random
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.preprocessing import image
import numpy as np

# Paths
train_dir = 'dataset/train'
test_dir = 'dataset/test'

# Parameters
IMG_SIZE = (224, 224)
BATCH_SIZE = 8
EPOCHS = 5
LIMIT_PER_CLASS = 50  # 50 Cat + 50 Dog

# Function to load a limited number of images into numpy arrays
def load_limited_images(folder, limit_per_class):
    X, y = [], []
    classes = os.listdir(folder)
    for idx, cls in enumerate(classes):
        cls_folder = os.path.join(folder, cls)
        images = os.listdir(cls_folder)
        selected = random.sample(images, min(limit_per_class, len(images)))
        for img_file in selected:
            img_path = os.path.join(cls_folder, img_file)
            img = image.load_img(img_path, target_size=IMG_SIZE)
            img_array = image.img_to_array(img) / 255.0
            X.append(img_array)
            y.append(idx)
    X = np.array(X)
    y = tf.keras.utils.to_categorical(y, num_classes=len(classes))
    return X, y, classes

# Load limited training and test data
X_train, y_train, CLASS_LABELS = load_limited_images(train_dir, LIMIT_PER_CLASS)
X_test, y_test, _ = load_limited_images(test_dir, LIMIT_PER_CLASS//5)  # smaller test set

# Load MobileNetV2
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224,224,3))
base_model.trainable = False

# Build model
model = Sequential([
    base_model,
    Flatten(),
    Dense(128, activation='relu'),
    Dense(len(CLASS_LABELS), activation='softmax')
])

# Compile
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Callbacks
os.makedirs('model', exist_ok=True)
checkpoint = ModelCheckpoint('model/model.h5', monitor='val_accuracy', save_best_only=True, verbose=1)
early_stop = EarlyStopping(monitor='val_accuracy', patience=3, restore_best_weights=True)

# Train
model.fit(
    X_train, y_train,
    validation_data=(X_test, y_test),
    epochs=EPOCHS,
    batch_size=BATCH_SIZE,
    callbacks=[checkpoint, early_stop]
)

print("Training complete. Model saved as model/model.h5")
