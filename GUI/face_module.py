# face_recognition_module.py

import time
import cv2
import face_recognition
import os
import joblib
import csv
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

def extract_info_from_filename(filename):
    """Extracts name, empID, and image number from the filename."""
    parts = os.path.splitext(filename)[0].split('_')
    if len(parts) == 3:
        name, emp_id, image_no = parts
        return name, emp_id
    else:
        return None, None

def train_face_recognition(dataset_path, model_save_path="trained_model.joblib"):
    """Train the face recognition model using images in the given dataset path."""
    a = time.time()
    known_faces = []
    known_names = []
    known_ids = []

    if os.path.exists(model_save_path):
        print("Loading pre-trained model...")
        try:
            known_faces, known_names, known_ids = joblib.load(model_save_path)
            return known_faces, known_names, known_ids
        except Exception as e:
            print(f"Error loading pre-trained model: {e}")
            known_faces, known_names, known_ids = [], [], []

    print("Training the model...")

    def resize_image(image):
        """Resize image for faster processing."""
        return cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

    def process_image(image_path):
        """Process each image and extract face encodings."""
        try:
            image = face_recognition.load_image_file(image_path)
            image = resize_image(image)
            face_landmarks = face_recognition.face_landmarks(image)

            if face_landmarks:
                top, right, bottom, left = face_recognition.face_locations(image)[0]
                face_encoding = face_recognition.face_encodings(image, [(top, right, bottom, left)])[0]
                name, emp_id = extract_info_from_filename(os.path.basename(image_path))
                known_faces.append(face_encoding)
                known_names.append(name)
                known_ids.append(emp_id)
            else:
                print(f"No face detected in {image_path}")
        except Exception as e:
            print(f"Error processing image {image_path}: {e}")

    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        for person_name in os.listdir(dataset_path):
            person_path = os.path.join(dataset_path, person_name)

            if os.path.isdir(person_path):
                image_paths = [os.path.join(person_path, image_name) for image_name in os.listdir(person_path)]
                executor.map(process_image, image_paths)

    try:
        joblib.dump((known_faces, known_names, known_ids), model_save_path)
        print("Finished")
        print("Model took", time.time() - a, "seconds")
    except Exception as e:
        print(f"Error saving trained model: {e}")

    return known_faces, known_names, known_ids

def recognize_faces(known_faces, known_names, known_ids, test_image, marked_attendance, attendance_file):
    """Recognize faces in the test image and mark attendance."""
    # Find faces in the test image
    face_locations = face_recognition.face_locations(test_image)
    face_encodings = face_recognition.face_encodings(test_image, face_locations)

    for face_encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
        # Compare the face encoding with known faces
        matches = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.5)

        name = "Unknown"
        emp_id = "Unknown"

        # If a match is found, use the name and ID of the known face
        if True in matches:
            first_match_index = matches.index(True)
            name = known_names[first_match_index]
            emp_id = known_ids[first_match_index]

            # Mark attendance only once for each person
            mark_attendance(name, emp_id, marked_attendance, attendance_file)

        # Draw rectangle, name, and ID on the frame
        cv2.rectangle(test_image, (left, top), (right, bottom), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(test_image, f"{name} ({emp_id})", (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    return test_image

def mark_attendance(name, emp_id, marked_attendance, attendance_file):
    """Mark attendance in the CSV file."""
    if name != "Unknown" and emp_id != "Unknown" and (name, emp_id) not in marked_attendance:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        attendance_data = [name, emp_id, current_time]

        # Append attendance data to the specified CSV file
        with open(attendance_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(attendance_data)

        marked_attendance.add((name, emp_id))  # Keep track of marked attendance

        print(f"Attendance marked for {name} (ID: {emp_id}) at {current_time}")

def start_recognition(dataset_path="images", attendance_file=None):
    """Start face recognition and attendance marking in a live camera feed."""
    # Train face recognition model
    known_faces, known_names, known_ids = train_face_recognition(dataset_path)

    # Open camera
    video_capture = cv2.VideoCapture(0)

    # Create a new attendance file for each day if not provided
    if attendance_file is None:
        attendance_file = f"attendance_{datetime.now().strftime('%Y-%m-%d')}.csv"

    # Initialize a set to track marked attendance
    marked_attendance = set()

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # Recognize faces and update display
        result_frame = recognize_faces(known_faces, known_names, known_ids, frame, marked_attendance, attendance_file)

        # Display the output frame
        cv2.imshow('Face Recognition Attendance System', result_frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close windows
    video_capture.release()
    cv2.destroyAllWindows()
