import cv2

def fetch_camera_feed():
    camera = cv2.VideoCapture(0)  # 0 for default camera
    if not camera.isOpened():
        raise Exception("Cannot access camera")
    return camera
