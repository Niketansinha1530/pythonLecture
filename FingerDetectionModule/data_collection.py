import cv2
import os

# Create folders for each class (0 to 5 fingers)
for i in range(6):
    os.makedirs(f"data/{i}", exist_ok=True)

# Initialize webcam
cap = cv2.VideoCapture(0)

# Dictionary to store counters for each folder
counters = {str(i): 0 for i in range(6)}  # Keys: '0', '1', '2', ..., '5'

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Display the frame
    cv2.imshow("Capture Images", frame)

    # Save image on pressing a key (0 to 5)
    key = cv2.waitKey(1) & 0xFF
    if key in [ord(str(i)) for i in range(6)]:  # Check if key is 0, 1, 2, 3, 4, or 5
        folder = str(key - ord('0'))  # Convert key to folder name (0 to 5)
        image_name = f"{counters[folder]}.jpg"  # Use the folder-specific counter
        cv2.imwrite(f"data/{folder}/{image_name}", frame)
        print(f"Saved image in folder {folder} as {image_name}")
        counters[folder] += 1  # Increment the folder-specific counter

    # Exit on 'q' key press
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()