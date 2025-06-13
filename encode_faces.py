import os
import cv2
import face_recognition
import pickle

def encode_faces(image_dir='images'):
    known_encodings = []
    known_names = []

    for filename in os.listdir(image_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img_path = os.path.join(image_dir, filename)
            image = cv2.imread(img_path)
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            boxes = face_recognition.face_locations(rgb)
            encodings = face_recognition.face_encodings(rgb, boxes)

            if encodings:
                known_encodings.append(encodings[0])
                known_names.append(os.path.splitext(filename)[0])

    with open("encodings.pickle", "wb") as f:
        pickle.dump({"encodings": known_encodings, "names": known_names}, f)

if __name__ == "__main__":
    encode_faces()
