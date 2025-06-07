import face_recognition
import os
import cv2
import pickle
from tqdm import tqdm

dataset_dir = 'faces'
encoding_file = 'face_encodings.pkl'

known_encodings = []
known_names = []

print("[INFO] Encoding faces...")
for person_name in os.listdir(dataset_dir):
    person_folder = os.path.join(dataset_dir, person_name)
    if not os.path.isdir(person_folder):
        continue

    print(f"[INFO] Processing: {person_name}")
    for img_name in tqdm(os.listdir(person_folder)):
        img_path = os.path.join(person_folder, img_name)
        img = cv2.imread(img_path)
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        boxes = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, boxes)

        for encoding in encodings:
            known_encodings.append(encoding)
            known_names.append(person_name)

# Save as tuple
with open(encoding_file, 'wb') as f:
    pickle.dump((known_encodings, known_names), f)

print(f"[INFO] Encoded {len(known_encodings)} faces. Data saved to {encoding_file}")
