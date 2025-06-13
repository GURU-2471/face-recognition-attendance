import cv2
import face_recognition
import numpy as np
import pickle
import pandas as pd
from datetime import datetime

def mark_attendance(name):
    try:
        data = pd.read_csv("attendance.csv")
    except FileNotFoundError:
        data = pd.DataFrame(columns=["Name", "Time"])

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if name not in data['Name'].values:
        new_entry = pd.DataFrame([[name, now]], columns=["Name", "Time"])
        data = pd.concat([data, new_entry])
        data.to_csv("attendance.csv", index=False)
        print(f"{name} marked present at {now}")

def main():
    with open("encodings.pickle", "rb") as f:
        data = pickle.load(f)

    video = cv2.VideoCapture(0)
    print("[INFO] Starting camera...")

    while True:
        ret, frame = video.read()
        if not ret:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, boxes)

        for encoding, box in zip(encodings, boxes):
            matches = face_recognition.compare_faces(data["encodings"], encoding)
            name = "Unknown"

            if True in matches:
                matched_idxs = [i for i, match in enumerate(matches) if match]
                counts = {}
                for i in matched_idxs:
                    counts[data["names"][i]] = counts.get(data["names"][i], 0) + 1
                name = max(counts, key=counts.get)

                mark_attendance(name)

            top, right, bottom, left = box
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)

        cv2.imshow("Attendance System", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
