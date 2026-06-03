# motion_detection.py
"""Motion Detection using OpenCV.

This script captures video from the default camera, detects motion using
frame differencing with an adaptive background, and highlights regions
where motion is detected. It demonstrates a lightweight approach suitable
for quick prototyping or integration into larger projects.

Dependencies:
    - opencv-python (`pip install opencv-python`)
    - numpy (`pip install numpy`)

Run the script and press 'q' to exit the video window.
"""

import cv2
import numpy as np

def main():
    # Initialize video capture (0 = default webcam)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video capture.")
        return

    # Read the first frame to establish the background model
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to read from camera.")
        cap.release()
        return
    # Convert to grayscale and blur to reduce noise
    prev_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    prev_gray = cv2.GaussianBlur(prev_gray, (21, 21), 0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert current frame to grayscale and blur
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        # Compute absolute difference between current frame and previous frame
        frame_delta = cv2.absdiff(prev_gray, gray)
        thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
        # Dilate the thresholded image to fill in holes
        thresh = cv2.dilate(thresh, None, iterations=2)

        # Find contours (i.e., areas of motion)
        contours, _ = cv2.findContours(
            thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        for cnt in contours:
            # Ignore small movements
            if cv2.contourArea(cnt) < 500:
                continue
            # Compute bounding box and draw it on the original frame
            (x, y, w, h) = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(
                frame,
                "Motion",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                2,
            )

        # Show the processed frames
        cv2.imshow("Motion Detection", frame)
        cv2.imshow("Threshold", thresh)

        # Update the previous frame for the next iteration
        prev_gray = gray.copy()

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cleanup resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
