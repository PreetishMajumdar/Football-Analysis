from ultralytics import YOLO
import cv2

# Load a pre-trained YOLO model
model = YOLO("yolo11n.pt")

# Start tracking objects in a video
# You can also use live video streams or webcam input
model.track(source="Datasets\\1.mp4")