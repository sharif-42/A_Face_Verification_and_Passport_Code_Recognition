# A face verification And Passport code recognition

This System verify passport code against the specific person. we used Face Recognition module for 
recognizing the face, and Pytesseract module for extracting passport code from the passport images. 
After that I verify the face against the passport code.

## Install the Followings
~~~~
sudo apt update
pip install opencv-python
pip install Pillow==2.2.1
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev
pip3 install face_recognition
~~~~
sometime Face Recognition Module May produce error when installing. The Try the following
~~~~
pip3 install CMake
pip3 install face_recognition
~~~~

## Download Traindata 
sometime we have to deal with local language. For this purpose tessaract provide the amazing faciclity.
Download the traindata from here 
**[Traindata](https://github.com/tesseract-ocr/tessdata/blob/master/script/Bengali.traineddata)**.

**Note:** This is only for support Bengali Language. Here is all **[Traindata](https://github.com/tesseract-ocr/tessdata)**.

## Set Path For Traindata
~~~~
Step 1: Downlaod Data TrainData
Step 2: Copy The Downloaded Traindata Path and Set is like the example.
        sudo cp <downlaoded_traindata_path> /usr/share/tesseract-ocr/4.00/tessdata
~~~~

## Set Up Important Parameter To Get Best Result.
#### Setup Config Parameter
~~~~
config = ("-l eng --oem 1 --psm 7")
~~~~
- **-l** represent the language Parameter, That is in which language we want to work with. Default English,
         If you want to work with other labguage then please have a look **[Here]()**.
         
- **--oem**  This set of traineddata files has support for the legacy recognizer with --oem 0 and 
            for LSTM models with --oem 1. For More See 
            **[Here](https://github.com/tesseract-ocr/tesseract/wiki/Data-Files#data-files-for-version-400-november-29-2016)**

- **--psm** Stands Page Segmentation Modes(psm). This is also another important parameter. To Know more take a look 
            **[Here](https://github.com/tesseract-ocr/tesseract/wiki/Command-Line-Usage)**.
            
## Workflow or Get Info From Image
 There is so many ways how you get information from image. Some Examples are,
 
- No Configuration Just Extract the information as String.
~~~~
data = str(pytesseract.image_to_string(image))
~~~~
- Get Dictionary Data
~~~~
data = pytesseract.image_to_string(image, output_type='dict')
~~~~
- Get Specific Languages data
~~~~
# Deafault English
config = ("-l ben --oem 1 --psm 7")
data = pytesseract.image_to_string(image, output_type='dict')
~~~~

- Get Multiple Languages data
~~~~
config = ("-l ben+eng --oem 1 --psm 3")
data = pytesseract.image_to_string(self.image, config=config, output_type='dict')
~~~~

## Used Tools
- **Python**.
- **Face Recognition Module** for Detect and Recognize Face(Developed by Facebook).
- **Opencv-Python** for Image Processing.
- **Pillow** for Image Processing.
- **Py-tessaract** for Data/Text Extraction from Image.