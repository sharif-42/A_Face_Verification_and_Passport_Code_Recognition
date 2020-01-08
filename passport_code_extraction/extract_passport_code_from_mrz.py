import cv2
import pytesseract


class OcrService:
    def __init__(self, image=None):
        print("OCR service Constructor Calling")
        self.image = image

    def extract_passport_code(self):
        config = ("-l eng --oem 1 --psm 7")
        data = pytesseract.image_to_string(self.image, output_type='dict')
        # s = str(pytesseract.image_to_string(img))
        # data = pytesseract.image_to_string(self.image, config=config, lang='Bengali', output_type='dict')
        return data


if __name__ == '__main__':
    image = cv2.imread('output_image_dataset/output.jpg', 0)  # read gray-scale image
    ocr_service = OcrService(image)
    cv2.imshow('image', image)
    cv2.waitKey(0)
    data = ocr_service.extract_passport_code()['text']
    print(data)
