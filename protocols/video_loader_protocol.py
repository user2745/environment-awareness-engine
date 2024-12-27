import cv2

def load_video(file_path):
    cap = cv2.VideoCapture(file_path)
    if not cap.isOpened():
        raise RuntimeError(f"Unable to open video file: {file_path}")
    return cap
def get_frame(cap):
    ret, frame = cap.read()
    if not ret:
        raise RuntimeError("Unable to read next frame from video.")
    return frame

def release_video(cap):
    cap.release()