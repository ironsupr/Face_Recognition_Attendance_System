# Face Recognition Attendance System

This project implements a face recognition-based attendance system using Python. The system captures and processes facial images from a webcam, matches them with previously saved images, and marks attendance accordingly. The system stores attendance data in a CSV file for later use.

## Features
- **Face Recognition**: The system uses facial recognition to identify employees/students and mark their attendance.
- **Real-time Camera Processing**: The system continuously captures frames from the webcam and processes them to detect and recognize faces.
- **Attendance Tracking**: Recognized faces are logged with the date and time in a CSV file.
- **Training Phase**: A training phase where the model is trained on images of the users' faces.
- **Parallel Processing**: The training process uses multi-threading to speed up face recognition.

## Files Overview

### 1. **face.py**
This file contains the core functionality of the face recognition system:
- **Train Face Recognition Model**: This function (`train_face_recognition`) trains the model by processing images from a dataset.
- **Recognize Faces**: Recognizes faces in real-time and compares them with known faces stored in the trained model.
- **Mark Attendance**: If a recognized face matches a stored face, attendance is marked and saved to a CSV file.

### 2. **save_images.py**
This script allows users to capture and save images for the training phase:
- **Capture and Save Images**: This function (`capture_and_save_images`) captures images from the webcam and saves them with user-specific filenames (name, roll number, and image number).
- **Directory Creation**: Saves images in a directory structure based on the user’s name and roll number.

## Installation

### Requirements
- Python 3.x
- Libraries: 
  - OpenCV (`cv2`)
  - face_recognition
  - joblib
  - csv
  - time
  - os
  - datetime
  - concurrent.futures

You can install the required libraries using the following command:

```bash
pip install opencv-python face_recognition joblib
```

### Directory Structure

```
project/
│
├── images/                  # Directory to store images for training
│   └── <name>/              # User-specific subdirectory containing captured images
├── trained_model.joblib     # Saved trained face recognition model
├── attendance_<date>.csv    # Generated attendance CSV file for each day
├── face.py                  # Main program for face recognition and attendance
└── save_images.py           # Program to capture and save images for training
```

## Usage

### Step 1: Capture and Save Images (Training Phase)
To train the system, first, run `save_images.py` to capture facial images. This will create a folder with the user’s name and roll number, where images will be saved.

```bash
python save_images.py
```

You will be prompted to enter the user's name and roll number. The script will automatically capture and save 100 images (or the specified number) from the webcam.

### Step 2: Train the Face Recognition Model
Once you have captured enough images, run the `face.py` script to train the face recognition model.

```bash
python face.py
```

This script will:
- Load existing trained data (if available).
- Train a model using the images saved in the `images/` directory.
- Save the trained model as `trained_model.joblib`.

### Step 3: Start Face Recognition and Mark Attendance
After training the model, the script will start the webcam feed. It will continuously recognize faces and mark attendance.

- The system will recognize faces from the webcam feed and compare them with the trained model.
- If a match is found, the attendance will be logged in a CSV file named with the current date (e.g., `attendance_2024-11-23.csv`).
- To stop the program, press the `q` key.

### Example

Run the following command to execute the system:

```bash
python face.py
```

The webcam feed will open, and the system will process faces. Each recognized face will be marked for attendance with the current date and time.

### Attendance File

The attendance will be logged in a CSV file, with each entry containing:
- **Name**
- **Roll Number**
- **Timestamp**

Example CSV content:

```
John Doe, 12345, 2024-11-23 10:15:30
Jane Smith, 67890, 2024-11-23 10:16:00
```

## Notes
- Ensure that the images you use for training are clear and well-lit for better recognition accuracy.
- The system can recognize multiple faces in a single frame and mark attendance for each recognized face.
- Attendance is marked only once for each person per session.

## Troubleshooting
- If no faces are detected during training or recognition, make sure the lighting is good and the camera is functioning properly.
- If the `trained_model.joblib` file is not found, make sure to run the training process first (`python face.py`).

## Contributions
Feel free to fork this project and submit pull requests if you'd like to contribute. Any improvements are welcome!
