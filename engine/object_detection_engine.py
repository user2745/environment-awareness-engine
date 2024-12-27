from protocols.camera_feed_protocol import start_camera_feed, get_frame_from_feed, release_camera_feed
from protocols.camera_protocol import fetch_camera_feed
from modules.object_detection import detect_objects

def run_object_detection(cap, model, labels):
    frame = get_frame_from_feed(cap)
    return detect_objects(frame, model, labels)

