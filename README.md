📸 Face Recognition Attendance System

🔍 Project Overview
The Face Recognition Attendance System is a computer vision-based project that automates attendance tracking using facial recognition. It leverages the face_recognition and OpenCV libraries to detect and identify individuals from a webcam feed. Once a known face is recognized, the system logs the person’s name along with the current date and time into a CSV file, effectively recording their attendance.

The system works offline and is ideal for schools, offices, or any scenario where reliable and contactless attendance is required.

🧱 Key Components
✅ Dependencies:
The system is built using python 3.10 :

face_recognition: for detecting and recognizing faces using deep learning

OpenCV: for real-time webcam video processing

NumPy, os, datetime, and pandas: for utility functions and data logging

🗂️ Data Collection and Preprocessing:
Image Folder (Images/):
A folder of labeled images is used where each image filename represents the person's name.

Encoding Faces:
Known faces are loaded and encoded using a 128-d vector from the face_recognition library. These encodings are stored and used for future comparisons.

🔒 Label Encoding:
Each image in the dataset is associated with a person's name (extracted from the file name).

These names act as identifiers when a face is matched during real-time recognition.

📐 Feature Extraction:
Facial encodings (128-dimensional vectors) serve as the feature representation of each known face.

These are compared in real-time with encodings extracted from the live webcam feed using Euclidean distance.

🧠 Real-Time Recognition & Logging:
The webcam captures frames continuously.

Faces detected in the frame are encoded and compared with the known encodings.

If a match is found:

The name is displayed on-screen using OpenCV.

The name and timestamp are stored in a CSV file (attendance.csv).

Duplicate entries are prevented within a session.

🧪 Model Evaluation:
Though it is not a machine learning model in the classical sense, the system performs accurately under normal lighting and camera conditions. Using face_recognition's HOG or CNN-based detector, it achieves high recognition accuracy in real-time scenarios.

🔁 Building a Live Attendance System:
Once setup is complete:

New users can be added by placing their labeled images into the Images/ folder and rerunning the encoding script.

Attendance is automatically logged for recognized individuals.

🚀 Usage
📁 Data Preparation:
Place known user images inside a folder named Images/.

Image filenames should match the person’s name (e.g., John.jpg, Alice.png).

🧠 Encoding Known Faces:
Run the encodes.py script to generate facial encodings from known images.

🎥 Running Attendance System:
Run main.py to start the webcam-based recognition and auto-attendance logging.

🛠️ Installation
Install the required Python libraries:

bash
Copy
Edit
pip install face_recognition opencv-python numpy pandas
Ensure you have Python 3.10+ installed, and your webcam is working.

✅ Conclusion
The Face Recognition Attendance System offers a simple yet powerful way to automate attendance tracking using facial recognition. Built entirely in Python and leveraging real-time computer vision, it provides a contactless, efficient, and scalable attendance solution that can be used in classrooms, offices, or even homes.

By following the modular scripts and structure, users can easily extend or deploy their own version of the system.

