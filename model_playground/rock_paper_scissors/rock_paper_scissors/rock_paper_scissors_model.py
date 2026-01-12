from ultralytics import YOLO
import cv2
import os
import math
from huggingface_hub import hf_hub_download
from datetime import datetime


def get_rock_paper_scissors():
    CONFIDENCE_THRESHOLD = 0.60
    DETECTION_TARGET = 5

    # Create a directory to store the saved images if it doesn't exist
    SAVE_DIR = "saved_images"
    os.makedirs(SAVE_DIR, exist_ok=True)

    # Create a dict to store the counts for each class
    detection_counts = {"rock": 0, "paper": 0, "scissors": 0}

    # Flag to signal when to exit and variable to store the result
    final_detection = None

    # start the camera
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    # Load the weights from repo
    model_path = hf_hub_download(
        local_dir=".",
        repo_id="fairportrobotics/rock-paper-scissors",
        filename="model.pt"
    )
    model = YOLO(model_path)

    # object classes
    classNames = ["rock", "paper", "scissors"]

    target_reached = False

    while True:
        success, img = cap.read()
        results = model(img, stream=True)

        for r in results:
            boxes = r.boxes

            for box in boxes:
                # Bounding box and confidence
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                confidence = math.ceil((box.conf[0] * 100)) / 100
                cls = int(box.cls[0])
                label = classNames[cls]

                # DRAW frame
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
                cv2.putText(img, f"{label} {confidence:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

                # SAVE the image
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
                filename = f"pre-check_{label}_{confidence:.2f}_{timestamp}.jpg"
                filepath = os.path.join(SAVE_DIR, filename)
                cv2.imwrite(filepath, img)

                # Check if confidence is high enough
                if confidence > CONFIDENCE_THRESHOLD:
                    # Increment the count
                    detection_counts[label] += 1

                    # Check has reached its target count
                    if detection_counts[label] >= DETECTION_TARGET:
                        final_detection = label
                        target_reached = True
                        print(f"\nTarget of {DETECTION_TARGET} reached for '{label}'! Exiting...")
                        break

            if target_reached:
                break

        # Exit if target count has been reached
        if target_reached:
            break

    # Clean up
    cap.release()
    cv2.destroyAllWindows()

    # Final
    if final_detection:
        print(f"\nFinal Confirmed Detection: {final_detection}")
        return final_detection
