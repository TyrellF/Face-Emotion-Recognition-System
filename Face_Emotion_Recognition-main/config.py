# TECH HUNTERS - Emotion Detection Configuration

# Application Settings
APP_NAME = "TECH HUNTERS Emotion Detection"
VERSION = "2.0"
DEBUG = True
HOST = "0.0.0.0"
PORT = 5000

# Model Settings
MODEL_WEIGHTS_FILE = "emotiondetector.h5"
MODEL_CONFIG_FILE = "emotiondetector.json"
INPUT_SIZE = (48, 48)
NUM_EMOTIONS = 7

# Camera Settings
CAMERA_INDEX = 0  # Default camera (0 for built-in, 1+ for external)
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
FPS = 30

# Detection Settings
CONFIDENCE_THRESHOLD = 0.5
FACE_SCALE_FACTOR = 1.3
MIN_NEIGHBORS = 5

# UI Settings
WINDOW_NAME = "TECH HUNTERS - Emotion Detection"
FONT = "cv2.FONT_HERSHEY_SIMPLEX"
FONT_SCALE = 0.8
FONT_COLOR = (0, 255, 0)  # Green
FONT_THICKNESS = 2
RECTANGLE_COLOR = (255, 0, 0)  # Blue
RECTANGLE_THICKNESS = 2

# Emotion Labels
EMOTION_LABELS = {
    0: "Angry",
    1: "Disgust", 
    2: "Fear",
    3: "Happy",
    4: "Neutral",
    5: "Sad",
    6: "Surprise"
}

# Team Information
TEAM_MEMBERS = [
    {
        "name": "Devesh Bhandari",
        "role": "AI/ML Developer",
        "specialization": "Deep Learning Specialist"
    },
    {
        "name": "Mohit Mehta", 
        "role": "Computer Vision Engineer",
        "specialization": "Image Processing Expert"
    },
    {
        "name": "Tyrell Fernandes",
        "role": "Full Stack Developer", 
        "specialization": "Web Development Lead"
    },
    {
        "name": "Anjali Rai",
        "role": "Data Scientist",
        "specialization": "Model Training Specialist"
    }
]
