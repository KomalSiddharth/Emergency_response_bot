import cv2
import time
from datetime import datetime

def capture_image():
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Use DirectShow backend
    time.sleep(2)

    ret, frame = cam.read()
    if not ret:
        print("❌ Camera access failed.")
        return None

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"emergency_{timestamp}.jpg"
    cv2.imwrite(filename, frame)
    cam.release()
    print(f"✅ Image captured and saved as {filename}")
    return filename


# Test function
if __name__ == "__main__":
    capture_image()
