from protocols.camera_feed_protocol import start_camera_feed, get_frame_from_feed
from protocols.video_loader_protocol import load_video
from modules.object_detection import detect_objects
from modules.activity_recognition import recognize_activity
from modules.context_aggregator import aggregate_context
import os
import json

class CoreEngine:
    def __init__(self):
        # Initialize components
        self.camera_feed = None
        self.model = None
        self.labels = None

    def initialize_engine(self, model_path, labels_path):
        """
        Initialize object detection model and labels.
        """
        import cv2
        self.model = cv2.dnn.readNetFromONNX(model_path)
        with open(labels_path, "r") as file:
            self.labels = file.read().splitlines()

    def process_environment(self):
        """
        Process the physical environment using the camera feed.
        """
        if not self.camera_feed:
            self.camera_feed = start_camera_feed()

        frame = get_frame_from_feed(self.camera_feed)
        objects = detect_objects(frame, self.model, self.labels)

        # For activity recognition, we would need a series of frames.
        activity = recognize_activity([frame])

        # Aggregate context for final report
        context = aggregate_context(objects, activity)
        return context

    def save_state(self, file_path):
        """
        Save the system state (e.g., detected objects) to a file.
        """
        state = {
            "camera_feed_status": "active" if self.camera_feed else "inactive"
        }
        with open(file_path, "w") as file:
            json.dump(state, file)
        print("System state saved.")

    def load_state(self, file_path):
        """
        Load the system state from a file.
        """
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                state = json.load(file)
                print("Loaded previous system state:", state)

    def close_resources(self):
        """
        Release resources such as camera feeds.
        """
        if self.camera_feed:
            self.camera_feed.release()
            self.camera_feed = None
