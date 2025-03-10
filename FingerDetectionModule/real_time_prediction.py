import cv2
import numpy as np
import tensorflow as tf

# Load the trained model

model = tf.keras.models.load_model("finger_count_model.h5")

#initialize the camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocess the frame (resize,gray scale,normalize)
    processed_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    processed_frame = cv2.resize(processed_frame, (64, 64))
    processed_frame = processed_frame / 255.0
    processed_frame = np.expand_dims(processed_frame, axis=(0, -1)) # Add batch and channel dimension


    # Predict the number of fingers
    prediction = model.predict(processed_frame)
    finger_count = np.argmax(prediction)

    # Display the result

    cv2.putText(frame, f"Finger Count: {finger_count}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Finger Count", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()