import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Load model dan label
model = load_model('keras_model.h5')
with open("labels.txt", "r") as f:
    class_labels = [line.strip() for line in f.readlines()]

IMG_SIZE = 224

def predict_image(img):
    img_resized = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img_array = img_to_array(img_resized) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    prediction = model.predict(img_array)[0]
    label_index = np.argmax(prediction)
    confidence = prediction[label_index]
    return class_labels[label_index], confidence

def detect_spots(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = np.array([10, 50, 50])
    upper = np.array([30, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        if cv2.contourArea(cnt) > 500:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    return image

class GreenGuardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌿 Greenguard - Deteksi Penyakit Daun Cabai")
        self.root.geometry("900x600")
        self.style = ttk.Style("solar")

        self.frame = ttk.Frame(root, padding=20)
        self.frame.pack(fill=BOTH, expand=YES)

        self.title = ttk.Label(self.frame, text="🌿 Greenguard", font=("Helvetica", 22, "bold"))
        self.title.pack(pady=10)

        self.img_label = ttk.Label(self.frame)
        self.img_label.pack(pady=10)

        self.result_label = ttk.Label(self.frame, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=10)

        btn_frame = ttk.Frame(self.frame)
        btn_frame.pack(pady=10)

        self.upload_btn = ttk.Button(btn_frame, text="📂 Upload Gambar", command=self.upload_image, bootstyle=PRIMARY)
        self.upload_btn.grid(row=0, column=0, padx=10)

        self.camera_btn = ttk.Button(btn_frame, text="🎥 Kamera Langsung", command=self.start_camera, bootstyle=SUCCESS)
        self.camera_btn.grid(row=0, column=1, padx=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            image = cv2.imread(file_path)
            label, conf = predict_image(image)
            image = detect_spots(image)
            cv2.putText(image, f"{label} ({conf*100:.2f}%)", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            img_pil = Image.fromarray(image_rgb)
            img_pil = img_pil.resize((600, 400))
            img_tk = ImageTk.PhotoImage(img_pil)

            self.img_label.configure(image=img_tk)
            self.img_label.image = img_tk
            self.result_label.config(text=f"Hasil Deteksi: {label} ({conf*100:.2f}%)")

    def start_camera(self):
        cam = cv2.VideoCapture(0)
        cv2.namedWindow("Greenguard - Tekan Q untuk keluar")
        while True:
            ret, frame = cam.read()
            if not ret:
                break
            label, conf = predict_image(frame)
            frame = detect_spots(frame)
            cv2.putText(frame, f"{label} ({conf*100:.2f}%)", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            cv2.imshow("Greenguard - Tekan Q untuk keluar", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cam.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = ttk.Window(themename="minty")  # kamu bisa ganti tema: 'darkly', 'cyborg', 'minty', dll
    app = GreenGuardApp(root)
    root.mainloop()
