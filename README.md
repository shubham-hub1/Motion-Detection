# Motion Detection Script

## Overview
`motion_detection.py` is a lightweight Python program that uses **OpenCV** to capture video from your default webcam, detect motion in real time, and highlight moving regions with green bounding boxes.

## Features
- Real‑time motion detection using frame differencing.
- Simple visual feedback: live video window plus a threshold visualization.
- Adjustable sensitivity (change the contour area threshold in the script).
- Press **`q`** to quit.

## Prerequisites
Make sure you have Python 3.8+ installed. Install the required packages:
```bash
pip install opencv-python numpy
```

## Usage
1. Open a terminal and navigate to the project folder where the script resides:
```powershell
cd "e:\alhorithm abdul\MeditationApp-master"
```
2. Run the script:
```powershell
python motion_detection.py
```
   - If your camera is not the default device, modify `cv2.VideoCapture(0)` to the appropriate index.
   - The script opens two windows: **Motion Detection** (live feed with bounding boxes) and **Threshold** (binary mask of motion).
   - Press **`q`** to close the windows and stop the program.

## Customization
- **Sensitivity** – change the `if cv2.contourArea(cnt) < 500:` line to a lower value for detecting smaller motions.
- **Background Update** – currently the previous frame becomes the background each iteration. For a more stable background, replace `prev_gray = gray.copy()` with a running average.

## Troubleshooting
- **Camera not opening** – ensure your webcam is not being used by another application. Verify the device index (`0`) is correct.
- **Missing modules** – run the `pip install` command above.
- **Performance issues** – reduce the frame size or increase the blur kernel size.

---

