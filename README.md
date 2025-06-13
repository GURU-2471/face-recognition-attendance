Project Description: Face Recognition Attendance System

The Face Recognition Attendance System is a Python-based automated solution that replaces traditional attendance methods with a contactless, real-time face recognition system. It uses machine learning techniques to detect and recognize human faces via a webcam, verifying identity against a pre-encoded dataset of known individuals.

Key Highlights:
Face Detection & Recognition: Utilizes the face_recognition library built on dlib’s deep learning model for accurate facial recognition using 128-dimensional encodings.

Real-Time Camera Feed: Uses OpenCV to capture live video, detect multiple faces simultaneously, and match them against known images.

Automated Attendance Logging: Once a face is recognized, the system records the name, date, and time into a CSV file to maintain daily attendance logs.

Duplicate Prevention: Each recognized face is logged only once per session to prevent duplicate entries.

Offline Capability: The entire system runs locally without requiring internet connectivity or cloud services.

🛠️ Technologies Used:
Python 3.10+
face_recognition
OpenCV
NumPy, Pandas, datetime, os

Folder Structure Example:
FaceRecognitionAttendance/
├── attendance.py               # Main script for live recognition and attendance
├── encodes.py            # Script to encode known faces
├── Images/               # Folder of known faces (with names as file names)
├── attendance.csv        # Stores the attendance log
├── README.md             # Project overview and setup guide
├── requirements.txt      # List of required packages
