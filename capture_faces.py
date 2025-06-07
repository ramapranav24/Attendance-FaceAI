import cv2
import os

# Ask for the name once
name = input("Enter the name of the person: ").strip()
save_path = os.path.join("faces", name)

# Create the directory if it doesn't exist
os.makedirs(save_path, exist_ok=True)

# Start video capture
cap = cv2.VideoCapture(0)
print("[INFO] Starting webcam. Press 's' to save image, 'q' to quit.")

count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Capture - Press 's' to save", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        count += 1
        filename = f"{name}_{count}.jpg"
        filepath = os.path.join(save_path, filename)
        cv2.imwrite(filepath, frame)
        print(f"[SAVED] {filename}")

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print(f"[INFO] {count} images saved to {save_path}")
