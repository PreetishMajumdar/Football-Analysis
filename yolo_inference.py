from ultralytics import YOLO
import cv2

# Load a pre-trained YOLO model
model = YOLO("models/best.pt")

# Start tracking objects in a video
# You can also use live video streams or webcam input
model.predict(source="datasets/4.mp4", save=True)