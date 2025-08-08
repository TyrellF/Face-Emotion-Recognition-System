# Project Title: Emotion Detection System using Intel oneAPI

The Emotion Detection System using Intel oneAPI is an innovative project that leverages the power of Intel's oneAPI toolkit to develop an intelligent and real-time emotion detection system. This system aims to accurately analyze and classify facial expressions to determine the underlying emotions of individuals in images or video streams. By combining the capabilities of deep learning, computer vision, and Intel's hardware acceleration, this project will create a robust and efficient solution for emotion analysis.

Key Features and Components:
1. **Data Collection and Preprocessing:**
   Gather a diverse dataset of facial images depicting different emotions (happy, sad, angry, surprised, etc.). Preprocess the images by resizing, normalizing, and augmenting them to enhance the model's performance.

2. **Model Selection:**
   Choose a suitable deep learning architecture for the emotion detection task, such as Convolutional Neural Networks (CNNs) or Recurrent Neural Networks (RNNs). Leverage Intel's oneAPI Deep Neural Network Library (oneDNN) to optimize the model for efficient execution on Intel hardware.

3. **Model Training:**
   Train the chosen model using the preprocessed dataset. Implement techniques like transfer learning or fine-tuning to expedite training. Utilize Intel oneAPI tools like oneDNN and oneDAL (oneAPI Data Analytics Library) to optimize training performance and accuracy.

4. **Real-time Emotion Detection:**
   Develop a real-time application that captures video streams from a webcam or a recorded video. Implement the trained model to process frames and predict emotions in real-time. Intel oneAPI Video Processing Library (oneVPL) can be utilized for efficient video stream processing.

5. **Graphical User Interface (GUI):**
   Create an intuitive GUI to display the video stream along with the detected emotions overlaid on the faces. Intel oneAPI Rendering Toolkit (oneRT) can be employed for creating visually appealing and responsive interfaces.

6. **Performance Optimization:**
   Fine-tune the model and application to ensure optimal performance on Intel hardware, such as CPUs, GPUs, and specialized accelerators like Intel Xe Graphics. Utilize profiling tools from the oneAPI toolkit to identify bottlenecks and optimize code.

7. **Deployment:**
   Package the final application and its dependencies into a user-friendly installer. Test the application on various Intel-based systems to ensure compatibility and performance consistency.

8. **Documentation and User Guide:**
   Prepare comprehensive documentation that includes installation instructions, usage guidelines, explanation of the underlying technology, and potential troubleshooting steps.

9. **Ethical Considerations:**
   Address privacy and ethical concerns related to facial data collection and storage. Implement measures to ensure data security and user consent.

10. **Future Enhancements:**
    Explore potential enhancements, such as multi-person emotion detection, emotion tracking over time, or integrating the system with IoT devices.

By completing this project, you'll not only develop a functional emotion detection system but also gain valuable experience in utilizing Intel's oneAPI toolkit for optimizing deep learning models and creating high-performance applications. This system could find applications in areas like market research, user experience evaluation, mental health support, and more.

For the dataset we are using the # 🧠 TECH HUNTERS - AI-Powered Facial Emotion Recognition System

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0+-orange.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.0+-green.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-red.svg)

A state-of-the-art real-time facial emotion recognition system that uses deep learning to detect and classify human emotions from live camera feed with high accuracy.

## 🌟 Features

- **Real-Time Detection**: Instant emotion recognition with minimal latency
- **7 Emotion Classes**: Angry, Disgust, Fear, Happy, Neutral, Sad, Surprise
- **High Accuracy**: Trained on extensive datasets for superior performance
- **User-Friendly Interface**: Modern web-based UI with intuitive design
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Confidence Scores**: Shows prediction confidence for each emotion
- **Easy to Use**: One-click start with comprehensive user guidance

## 🎯 Detected Emotions

| Emotion | Emoji | Description |
|---------|-------|-------------|
| Angry | 😠 | Frustration, annoyance, anger |
| Disgust | 🤢 | Revulsion, distaste, aversion |
| Fear | 😨 | Anxiety, worry, apprehension |
| Happy | 😊 | Joy, satisfaction, contentment |
| Neutral | 😐 | Calm, composed, no strong emotion |
| Sad | 😢 | Sorrow, melancholy, unhappiness |
| Surprise | 😲 | Shock, amazement, astonishment |

## 🛠️ Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap
- **Backend**: Python Flask
- **Deep Learning**: TensorFlow/Keras
- **Computer Vision**: OpenCV
- **Face Detection**: Haar Cascade Classifiers
- **Model Architecture**: Convolutional Neural Network (CNN)

## 📋 Prerequisites

- Python 3.7 or higher
- Webcam/Camera
- Modern web browser

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/tech-hunters-emotion-detection.git
   cd tech-hunters-emotion-detection
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify model files exist**
   Ensure these files are in the project directory:
   - `emotiondetector.h5` (trained model weights)
   - `emotiondetector.json` (model architecture)

## 🎮 Usage

1. **Start the web application**
   ```bash
   python app.py
   ```

2. **Open your browser**
   Navigate to `http://localhost:5000`

3. **Start emotion detection**
   - Click the "Start Detection" button
   - Allow camera access when prompted
   - Look at the camera to see real-time emotion detection
   - Press ESC to stop detection

## 📊 How It Works

1. **Camera Input**: Captures live video from your webcam
2. **Face Detection**: Uses Haar Cascade to identify faces in the frame
3. **Preprocessing**: Resizes and normalizes face images to 48x48 pixels
4. **AI Analysis**: Deep learning model processes facial features
5. **Classification**: Predicts emotion with confidence scores
6. **Display**: Shows results in real-time on the video feed

## 🏗️ Model Architecture

The system uses a Convolutional Neural Network (CNN) trained on facial expression datasets:

- **Input Layer**: 48x48 grayscale images
- **Convolutional Layers**: Feature extraction with ReLU activation
- **Pooling Layers**: Dimensionality reduction
- **Dense Layers**: Classification with softmax output
- **Output**: 7 emotion classes with probability scores

## 🎨 UI Improvements

### Enhanced Features:
- **Modern Design**: Gradient backgrounds and glassmorphism effects
- **Responsive Layout**: Works on desktop, tablet, and mobile
- **Interactive Elements**: Hover effects and smooth animations
- **Better UX**: Loading states, error handling, and user guidance
- **Professional Styling**: Clean typography and consistent spacing

### Visual Enhancements:
- Emotion badges with emojis
- Technology showcase section
- Team member profiles
- Feature highlights
- Improved color scheme

## 👥 Development Team

| Developer | Role | Specialization |
|-----------|------|----------------|
| **Devesh Bhandari** | AI/ML Developer | Deep Learning Specialist |
| **Mohit Mehta** | Computer Vision Engineer | Image Processing Expert |
| **Tyrell Fernandes** | Full Stack Developer | Web Development Lead |
| **Anjali Rai** | Data Scientist | Model Training Specialist |

## 🔧 Configuration

### Camera Settings
- Default camera index: 0 (can be modified in `run_script.py`)
- Frame rate: 30 FPS
- Resolution: Auto-detected

### Model Parameters
- Input size: 48x48 pixels
- Color space: Grayscale
- Batch size: 1 (real-time)

## 🚨 Troubleshooting

### Common Issues:

1. **Camera not working**
   - Check camera permissions
   - Ensure camera is not used by other applications
   - Try different camera index (0, 1, 2...)

2. **Model not loading**
   - Verify `emotiondetector.h5` and `emotiondetector.json` exist
   - Check file permissions

3. **Poor detection accuracy**
   - Ensure good lighting
   - Position face clearly in camera view
   - Avoid obstructions

### Error Messages:
- `Model file not found`: Download or train the model
- `Camera access denied`: Grant camera permissions
- `No faces detected`: Adjust lighting and positioning

## 📈 Performance

- **Detection Speed**: ~30 FPS on modern hardware
- **Accuracy**: ~85% on validation datasets
- **Latency**: <100ms per frame
- **Memory Usage**: ~500MB with model loaded

## 🔒 Privacy

- **No Data Storage**: Emotions detected in real-time, no images saved
- **Local Processing**: All analysis happens on your device
- **No Network**: Works completely offline after initial setup

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Support

For support and questions:
- Create an issue in the GitHub repository
- Contact the development team
- Check the troubleshooting section

## 🙏 Acknowledgments

- **OpenCV Community** for computer vision tools
- **TensorFlow Team** for deep learning framework
- **Research Community** for emotion recognition datasets
- **Flask Team** for the web framework

---

<div align="center">
  <strong>Built with ❤️ by the TECH HUNTERS Team</strong>
  <br>
  <em>Emerging Digital Innovators from Bengaluru</em>
</div> dataset from kaggle : https://www.kaggle.com/datasets/jonathanoheix/face-expression-recognition-dataset

# oneAPI libraries used

intel-tensorflow

intel-numpy

opencv-python-headless
