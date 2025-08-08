# -*- coding: utf-8 -*-
import cv2
from keras.models import model_from_json
import numpy as np
import os
import sys

# Windows-specific imports for bringing window to front
if sys.platform == "win32":
    import ctypes
    from ctypes import wintypes

def bring_window_to_front(window_name):
    """Bring OpenCV window to front on Windows"""
    if sys.platform == "win32":
        try:
            # Get window handle
            hwnd = ctypes.windll.user32.FindWindowW(None, window_name)
            if hwnd:
                # Bring window to front
                ctypes.windll.user32.SetForegroundWindow(hwnd)
                ctypes.windll.user32.ShowWindow(hwnd, 9)  # SW_RESTORE
                ctypes.windll.user32.SetActiveWindow(hwnd)
                return True
        except Exception as e:
            print(f"[WARNING] Could not bring window to front: {e}")
    return False

def cleanup_resources(webcam, window_name):
    """Properly cleanup camera and windows"""
    try:
        if webcam and webcam.isOpened():
            webcam.release()
            print("[SUCCESS] Camera released")
        
        # Force close the specific window
        try:
            cv2.destroyWindow(window_name)
        except:
            pass
        
        # Force close all windows
        cv2.destroyAllWindows()
        
        # Additional cleanup for Windows
        if sys.platform == "win32":
            try:
                # Force close any remaining OpenCV windows
                for i in range(10):
                    cv2.waitKey(1)
            except:
                pass
        
        print("[SUCCESS] All windows closed")
    except Exception as e:
        print(f"[WARNING] Error during cleanup: {e}")

def load_model():
    """Load the emotion detection model"""
    try:
        json_file = open("emotiondetector.json", "r")
        model_json = json_file.read()
        json_file.close()
        model = model_from_json(model_json)
        model.load_weights("emotiondetector.h5")
        print("[SUCCESS] Model loaded successfully")
        return model
    except Exception as e:
        print(f"[ERROR] Error loading model: {e}")
        return None

def initialize_camera():
    """Initialize camera and face detection"""
    try:
        print("[INFO] Trying to access camera...")
        webcam = cv2.VideoCapture(0)
        
        # Set a timeout and try to read a frame to verify camera access
        webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        
        if not webcam.isOpened():
            raise Exception("Could not access camera. Please check if camera is connected and not being used by another application.")
        
        # Test reading a frame
        ret, test_frame = webcam.read()
        if not ret:
            raise Exception("Camera is connected but cannot read frames. Please check camera permissions.")
        
        haar_file = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        face_cascade = cv2.CascadeClassifier(haar_file)
        
        if face_cascade.empty():
            raise Exception("Could not load face detection classifier")
            
        print("[SUCCESS] Camera initialized successfully")
        print("[SUCCESS] Face detection classifier loaded")
        return webcam, face_cascade
    except Exception as e:
        print(f"[ERROR] Error initializing camera: {e}")
        print("[INFO] Please ensure:")
        print("  - Camera is properly connected")
        print("  - Camera is not being used by another application")
        print("  - Camera permissions are granted")
        return None, None

def extract_features(image):
    """Extract features from face image for emotion prediction"""
    feature = np.array(image)
    feature = feature.reshape(1, 48, 48, 1)
    return feature / 255.0

def main():
    """Main emotion detection function"""
    print("STARTING TECH HUNTERS Emotion Detection System...")
    print("=" * 50)
    
    # Load model
    model = load_model()
    if model is None:
        print("[FATAL] Cannot continue without model. Exiting...")
        return
    
    # Initialize camera
    webcam, face_cascade = initialize_camera()
    if webcam is None or face_cascade is None:
        print("[FATAL] Cannot continue without camera access. Exiting...")
        return
    
    # Emotion labels
    labels = {0: 'Angry', 1: 'Disgust', 2: 'Fear', 3: 'Happy', 4: 'Neutral', 5: 'Sad', 6: 'Surprise'}
    
    print("Camera feed started - Look at the camera!")
    print("Emotion detection is now active")
    print("*** CAMERA WINDOW SHOULD APPEAR AUTOMATICALLY ***")
    print("To stop detection:")
    print("  Press 'ESC' key")
    print("  Press 'Q' key") 
    print("  Click the 'X' button to close window")
    print("=" * 50)
    
    # Create window with specific properties
    window_name = "TECH HUNTERS - Emotion Detection"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
    cv2.resizeWindow(window_name, 800, 600)
    
    # Try to set window to topmost (this may not work on all systems)
    try:
        cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1)
    except:
        pass
    
    # Variable to track if window should close
    should_close = False
    
    frame_count = 0
    
    try:
        while True:
            ret, frame = webcam.read()
            if not ret:
                print("⚠️  Could not read frame from camera")
                break
                
            frame_count += 1
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(frame, 1.3, 5)
            
            # Process detected faces
            for (x, y, w, h) in faces:
                # Extract face region
                face_image = gray[y:y+h, x:x+w]
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                
                # Resize for model input
                face_image = cv2.resize(face_image, (48, 48))
                
                # Predict emotion
                features = extract_features(face_image)
                prediction = model.predict(features, verbose=0)
                emotion_label = labels[prediction.argmax()]
                confidence = np.max(prediction) * 100
                
                # Display emotion on frame
                label_text = f'{emotion_label} ({confidence:.1f}%)'
                cv2.putText(frame, label_text, (x-10, y-10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                
                # Print to console every 30 frames
                if frame_count % 30 == 0:
                    print(f"Detected: {emotion_label} (Confidence: {confidence:.1f}%)")
            
            # Show frame
            cv2.imshow(window_name, frame)
            
            # Bring window to front (try multiple times in first few frames)
            if frame_count <= 10:
                bring_window_to_front(window_name)
            
            # Check for multiple exit conditions with minimal delay
            key = cv2.waitKey(1) & 0xFF
            
            # ESC key pressed
            if key == 27:
                print("[STOPPED] Detection stopped by user (ESC key)")
                break
            
            # Q key pressed (alternative exit)
            if key == ord('q') or key == ord('Q'):
                print("[STOPPED] Detection stopped by user (Q key)")
                break
            
            # Window closed by clicking X button
            try:
                if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
                    print("[STOPPED] Detection stopped by user (window closed)")
                    break
            except cv2.error:
                # Window was destroyed
                print("[STOPPED] Detection stopped by user (window destroyed)")
                break
                
    except KeyboardInterrupt:
        print("[STOPPED] Detection interrupted by user (Ctrl+C)")
    except Exception as e:
        print(f"[ERROR] Error during detection: {e}")
    finally:
        # Proper cleanup
        cleanup_resources(webcam, window_name)
        print("Thank you for using TECH HUNTERS!")

if __name__ == "__main__":
    main()