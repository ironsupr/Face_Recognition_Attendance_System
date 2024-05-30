import cv2
import os
import time

def capture_and_save_images(name, roll_no, num_images_to_capture=5):
    # Open the default camera (index 0)
    cap = cv2.VideoCapture(0)

    # Create the 'images' directory if it doesn't exist
    images_dir = os.path.join(os.getcwd(), 'images')
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    image_number = 1
    while image_number <= num_images_to_capture:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Check if the frame was captured successfully
        if not ret:
            print("Error capturing frame. Exiting...")
            break

        # Display the resulting frame
        cv2.imshow('Capture Image', frame)

        # Save the captured image with the name in the path
        image_path = os.path.join(images_dir, name, f'{name}_{roll_no}_{image_number}.jpg')
        os.makedirs(os.path.dirname(image_path), exist_ok=True)
        cv2.imwrite(image_path, frame)
        print(f'Image {image_number} saved: {image_path}')

        image_number += 1
        time.sleep(0.2)

    # Release the camera
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Get user input for Name and Roll No.
    name = input("Enter Name: ")
    roll_no = input("Enter Roll No.: ")

    # Set the number of images to capture
    num_images_to_capture = 100

    # Capture and save images automatically
    capture_and_save_images(name, roll_no, num_images_to_capture)
