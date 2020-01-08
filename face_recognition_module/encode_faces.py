import face_recognition
import pickle
import cv2
import imutils

imagePath = "face_datasets/alan_grant/00000000.jpg"
image = cv2.imread(imagePath)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
resized_image = imutils.resize(rgb, height=600,width=700)
cv2.imshow('resized_image',resized_image)
cv2.waitKey(0)

# image = face_recognition.load_image_file("face_datasets/alan_grant/00000000.jpg")
# face_locations = face_recognition.face_locations(image)
