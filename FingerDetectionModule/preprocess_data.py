import cv2
import numpy as np
import os

#Define image size
IMG_SIZE = 64

#Load and preprocess the image

def preprocess_images(data_folder):
    X = [] #To store images
    y = [] #To store labels


    for folder in os.listdir(data_folder):
        folder_path = os.path.join(data_folder,folder)
        if not os.path.isdir(folder_path):
            continue
    
        label = int(folder) # Folder name is the label (0 to 5)
        for image_name in os.listdir(folder_path):
            image_path = os.path.join(folder_path,image_name)
            image = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE) # Convert to grayscale

            image = cv2.resize(image,(IMG_SIZE,IMG_SIZE)) # Resize the image 64 * 64
            image = image/255.0 # Normalize pixel values to [0 to 1]


            X.append(image)
            y.append(label)
    
    return np.array(X),np.array(y)

#Save the preprocessed data
X,y = preprocess_images("data")
np.save("X.npy",X)
np.save("y.npy",y)
print("Preprocessing Complete! Data saved X.npy and y.npy")

