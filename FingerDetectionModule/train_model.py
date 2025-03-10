import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

# Load the preprocessed data

X = np.load("X.npy")
y = np.load("y.npy")

# Reshape X to add to channel dimension ( required for CNN)
X = X.reshape(-1,64,64,1)

# Convert labels to one hot encoded format

y = tf.keras.utils.to_categorical(y,num_classes=6)

#Build the CNN model
model = models.Sequential([
    layers.Conv2D(32,(3,3),activation='relu',input_shape=(64,64,1)),
    layers.MaxPooling2D((2,2)),
    layers.Conv2D(64,(3,3),activation='relu'),
    layers.MaxPooling2D((2,2)),
    layers.Flatten(),
    layers.Dense(128,activation='relu'),
    layers.Dense(6,activation='softmax') #6 classes (0 to 5 fingers)
])

#Compile the model
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])

#Train the model
model.fit(X,y,epochs=10,batch_size=32,validation_split=0.2)

#Save the model
model.save("finger_count_model.h5")
print("Model trained and saved as finger_count_model.h5")