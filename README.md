# A face verification And Passport code recognition

This System verify passport code against the specific person. we used Face Recognition module for 
recognizing the face, and Pytesseract module for extracting passport code from the passport images. 
After that I verify the face against the passport code.

## Install the Followings
~~~~
sudo apt update
pip install opencv-python
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev
~~~~
## Download Traindata 
sometime we have to deal with local language. For this purpose tessaract provide the amazing faciclity.
Download the traindata from here 
**[Traindata](https://github.com/tesseract-ocr/tessdata/blob/master/script/Bengali.traineddata)**.
**Note:** This is only for support Bengali Language. Here is all **[Traindata](https://github.com/tesseract-ocr/tessdata) 

## Used Tools
- **Python**.
- **Face Recognition Module** for Detect and Recognize Face(Developed by Facebook).
- **Opencv-Python** for Image Processing.
- **Pillow** for Image Processing.
- **Py-tessaract** for Data/Text Extraction from Image.