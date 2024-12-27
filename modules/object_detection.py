import cv2
import numpy as np

def detect_objects(frame, model, labels):
    # Preprocess the frame
    blob = cv2.dnn.blobFromImage(frame, scalefactor=1/255.0, size=(416, 416), swapRB=True)
    model.setInput(blob)
    detections = model.forward()

    objects = []
    for detection in detections[0, 0, :, :]:
        confidence = detection[2]
        if confidence > 0.5:
            class_id = int(detection[1])
            x, y, w, h = detection[3:7]
            objects.append({"label": labels[class_id], "confidence": confidence, "bbox": (x, y, w, h)})
    return objects
