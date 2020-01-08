import face_recognition

image = face_recognition.load_image_file("faces_datasets/alan_grant/00000000.jpg")
face_locations = face_recognition.face_locations(image)
