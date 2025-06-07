# Attendance-FaceAI

A real-time face recognition-based attendance system developed using Python, OpenCV, and Flask. This project automates student attendance by detecting and recognizing faces from a webcam feed and logs each entry with a timestamp.

---

## Features

- Real-time face recognition using webcam  
- Logs attendance into a CSV file with name and timestamp  
- Prevents multiple entries for the same person in a single session  
- Flask-based web interface to mark and view attendance  
- Styled HTML/CSS frontend  
- Supports multiple users/faces  

---

## Technologies Used

- Python 3.8  
- OpenCV (cv2)  
- face_recognition (built on dlib)  
- Flask (web framework)  
- HTML & CSS (frontend styling)  
- Pickle and CSV (data handling)

---

## Project Structure

Attendance-FaceAI/
├── app.py                # Flask web application
├── capture_faces.py      # Script to capture face images
├── train_model.py        # Script to encode faces and save encodings
├── mark_attendance.py    # Script for real-time recognition and logging
├── face_encodings.pkl    # Stored face encodings using pickle
├── attendance.csv        # Attendance records (Name, Time)
├── faces/                # Directory of captured images
│   └── pranav/, sachit/  # Folders for each registered user
├── templates/
│   └── index.html        # Web interface template
├── static/
│   └── style.css         # Custom CSS styling

