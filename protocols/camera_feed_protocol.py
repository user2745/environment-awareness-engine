import cv2

def start_camera_feed(camera_index=0):
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        raise RuntimeError("Unable to access the camera feed.")
    return cap

def get_frame_from_feed(cap):
    ret, frame = cap.read()
    if not ret:
        raise RuntimeError("Failed to capture frame from camera.")
    return frame
    def release_camera_feed(cap):
        cap.release()
        cv2.destroyAllWindows()