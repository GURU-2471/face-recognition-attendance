# 📸 Face Recognition Attendance System

## 🔍 Project Overview

The **Face Recognition Attendance System** is a computer vision-based project that automates attendance tracking using facial recognition. It leverages the `face_recognition` and `OpenCV` libraries to detect and identify individuals from a webcam feed. Once a known face is recognized, the system logs the person’s name along with the current date and time into a CSV file, effectively recording their attendance.

The system works offline and is ideal for schools, offices, or any scenario where reliable and contactless attendance is required.

---

## 🧱 Key Components

### ✅ Dependencies

The system is built using **Python 3.10** and uses the following libraries:

- `face_recognition`: For detecting and recognizing faces using deep learning  
- `OpenCV`: For real-time webcam video processing  
- `NumPy`, `os`, `datetime`, `pandas`: For utility functions and data logging

---

### 🗂️ Data Collection and Preprocessing

#### 📁 Image Folder (`Images/`)
- A folder of labeled images is used where each image filename represents the person's name.

#### 📥 Encoding Faces
- Known faces are loaded and encoded using a **128-dimensional vector** from the `face_recognition` library.
- These encodings are stored and used for future comparisons.

---

### 🔒 Label Encoding

- Each image is labeled using the person’s name (extracted from the filename).
- These names act as identifiers during real-time recognition.

---

### 📐 Feature Extraction

- Facial encodings (128-d vectors) serve as feature representations of known faces.
- Real-time webcam encodings are compared to these using **Euclidean distance** for matching.

---

### 🧠 Real-Time Recognition & Logging

- Webcam captures frames continuously.
- Detected faces are encoded and compared with known encodings.
- If a match is found:
  - Name is displayed on screen using OpenCV.
  - Name and timestamp are logged in `attendance.csv`.
  - Duplicate entries are avoided within the same session.

---

### 🧪 Model Evaluation

- Although not a classical ML model, the system achieves **high accuracy** using HOG or CNN-based face detection (from `face_recognition`).
- Performs reliably under normal lighting and camera conditions.

---

## 🔁 Building a Live Attendance System

- Add new users by placing their images in the `Images/` folder.
- Re-run the encoding script to update facial data.
- Launch the system and attendance is logged automatically.

---

## 🚀 Usage

### 📁 Data Preparation

- Place known user images in a folder named `Images/`
- File names should match the person’s name (e.g., `John.jpg`, `Alice.png`)

### 🧠 Encoding Known Faces

```bash
python encodes.py
```
---
## 🎥 Running Attendance System

```bash
python main.py
```
---
## 🛠️ Installation

Install the required Python packages:

```bash
pip install face_recognition opencv-python numpy pandas
```
## ✅ Requirements

Make sure:

- ✅ You are using **Python 3.10 or above**
- ✅ Your **webcam is functioning correctly**

---

## ✅ Conclusion

The **Face Recognition Attendance System** offers a simple yet powerful solution to automate attendance tracking using facial recognition. Built entirely in **Python**, it leverages real-time computer vision to provide a:

- 📌 **Contactless**
- ⚡ **Efficient**
- 📈 **Scalable**

attendance solution suitable for:

- 🏫 **Classrooms**
- 🏢 **Offices**
- 🏠 **Home setups**

Its modular design makes it easy to **customize**, **extend**, or **deploy** for various real-world use cases.

---

## 🙋‍♂️ Author

**Gaurav Pavtekar**  
🔗 [GitHub Profile](https://github.com/GURU-2471)  
📧 Email: gauravpavtekar24@gmail.com

