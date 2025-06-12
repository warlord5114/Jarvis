import cv2
import numpy as np
from PIL import Image 
import os

base_dir = os.path.dirname(os.path.abspath(__file__))  # path to auth/
path = os.path.join(base_dir, 'samples')
recognizer = cv2.face.LBPHFaceRecognizer_create() 
detector = cv2.CascadeClassifier(os.path.join(base_dir, "haarcascade_frontalface_default.xml"))

def Images_And_Labels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path) if not f.startswith('.')]
    faceSamples = []
    ids = []

    for imagePath in imagePaths:
        gray_img = Image.open(imagePath).convert('L')
        img_arr = np.array(gray_img, 'uint8')

        try:
            id = int(os.path.split(imagePath)[-1].split(".")[1])
        except:
            print(f"[WARN] Skipping file {imagePath} — invalid name format")
            continue

        faces = detector.detectMultiScale(img_arr)
        print(f"Processing {imagePath} → Detected {len(faces)} face(s)")

        for (x, y, w, h) in faces:
            faceSamples.append(img_arr[y:y+h, x:x+w])
            ids.append(id)

    return faceSamples, ids

print("[INFO] Training faces. Please wait...")

faces, ids = Images_And_Labels(path)

if len(faces) == 0:
    print("[ERROR] No faces found. Training aborted.")
    exit()

recognizer.train(faces, np.array(ids))
recognizer.write(os.path.join(base_dir, 'trainer', 'trainer.yml'))

print("[SUCCESS] Model trained. You can now recognize faces.")
