import cv2
import numpy as np

# initialize a rectangular and square structuring kernel
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))
sqKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 21))


class MachineReadableZoneDetector:
    def __init__(self, image=None):
        print("Image Processing Services Calling")
        self.image = image
        pass

    @staticmethod
    def show_single_image(image):
        """
        A new Window will open with an image press any key for dismiss the window
        """
        cv2.imshow("image", image)
        cv2.waitKey(0)


if __name__ == '__main__':
    service = MachineReadableZoneDetector()
    image = cv2.imread('dataset/pass_port_1.jpg', 0)  # nid_front
    service.show_single_image(image)
