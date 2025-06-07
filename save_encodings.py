import face_recognition
import os
import pickle

# Path to the faces folder
faces_dir = "faces"

known_face_encodings = []
known_face_names = []

# Loop through each person in the faces directory
for filename in os.listdir(faces_dir):
    if filename.endswith((".jpg", ".png", ".jpeg")):
        # Extract person's name from the filename (without extension)
        name = os.path.splitext(filename)[0]

        # Load the image
        image_path = os.path.join(faces_dir, filename)
        image = face_recognition.load_image_file(image_path)

        # Get face encodings (assuming one face per image)
        encodings = face_recognition.face_encodings(image)

        if encodings:
            known_face_encodings.append(encodings[0])
            known_face_names.append(name)
        else:
            print(f"[WARNING] No face found in {filename}")

# Save the encodings and names to a pickle file
with open("face_encodings.pkl", "wb") as f:
    pickle.dump((known_face_encodings, known_face_names), f)

print("face_encodings.pkl saved successfully.")
