import face_recognition
import cv2
import pickle
import os
from datetime import datetime

# Load known encodings
with open("face_encodings.pkl", "rb") as f:
    known_face_encodings, known_face_names = pickle.load(f)

# Set to remember already logged names
logged_this_session = set()

def mark_attendance(name):
    if name == "Unknown":
        return

    if name in logged_this_session:
        return  # Already logged in this session

    logged_this_session.add(name)  # Mark this name as logged

    filename = "attendance.csv"
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            f.write("Name,Time\n")

    with open(filename, 'a') as f:
        f.write(f"{name},{dt_string}\n")
    print(f"[LOGGED] {name} at {dt_string}")

# Start webcam
print("[INFO] Starting webcam...")
video_capture = cv2.VideoCapture(0)

if not video_capture.isOpened():
    print("[ERROR] Could not open webcam.")
    exit()

print("[INFO] Webcam opened. Press 'q' to quit.")

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("[WARNING] Frame not captured — retrying...")
        continue

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.6)
            name = "Unknown"

            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            if len(face_distances) > 0:
                best_match_index = face_distances.argmin()
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

            face_names.append(name)

            # ✅ Only log once per session
            mark_attendance(name)

    process_this_frame = not process_this_frame

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 255, 0), cv2.FILLED)
        cv2.putText(frame, name, (left + 6, bottom - 6),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 1)

    cv2.imshow("Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
