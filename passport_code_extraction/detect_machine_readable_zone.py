import cv2
import imutils as imutils
import numpy as np


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

    @staticmethod
    def save_image(image):
        """
        Save the image to a specific location.
        """
        cv2.imwrite('output_image_dataset/gray.jpg', gray)


if __name__ == '__main__':
    service = MachineReadableZoneDetector()
    image = cv2.imread('passport_dataset/pass_port_1.jpg', 0)  # read gray-scale image
    image = imutils.resize(image, height=600)
    # initialize a rectangular and square structuring kernel
    rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))
    sqKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 21))

    """
    smooth the image using a 3x3 Gaussian, then apply the blackhat morphological operator to 
    find dark regions on a light background
    """
    gray = cv2.GaussianBlur(image, (3, 3), 0)
    cv2.imwrite('output_image_dataset/gray.jpg', gray)
    blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKernel)
    cv2.imwrite('output_image_dataset/blackhat.jpg', blackhat)

    """
    compute the Scharr gradient of the blackhat image and scale the result into the range [0, 255]  
    """

    gradX = cv2.Sobel(blackhat, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
    cv2.imwrite('output_image_dataset/gradX.jpg', gradX)

    gradX = np.absolute(gradX)
    (minVal, maxVal) = (np.min(gradX), np.max(gradX))
    gradX = (255 * ((gradX - minVal) / (maxVal - minVal))).astype("uint8")
    print(gradX)
    print(minVal, maxVal)

    """
    apply a closing operation using the rectangular kernel to close gaps in between letters -- then 
    apply Otsu's thresholding method
    """
    gradX = cv2.morphologyEx(gradX, cv2.MORPH_CLOSE, rectKernel)
    cv2.imwrite('output_image_dataset/gradX_.jpg', gradX)
    thresh = cv2.threshold(gradX, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    cv2.imwrite('output_image_dataset/thresh.jpg', thresh)
    """
    perform another closing operation, this time using the square kernel to close gaps between 
    lines of the MRZ, then perform a serieso of erosions to break apart connected components
    """
    morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, sqKernel)
    cv2.imwrite('output_image_dataset/morph.jpg', morph)
    erode = cv2.erode(morph, None, iterations=4)
    cv2.imwrite('output_image_dataset/erode.jpg', erode)

    """
    during thresholding, it's possible that border pixels were included in the thresholding, so let's set 5% of 
    the left and right borders to zero
    """
    p = int(image.shape[1] * 0.05)
    erode[:, 0:p] = 0
    erode[:, image.shape[1] - p:] = 0
    cv2.imwrite('output_image_dataset/erode_.jpg', erode)

    # find contours in the thresholded image and sort them by their size
    cnts = cv2.findContours(erode.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

    # loop over the contours
    for c in cnts:
        # compute the bounding box of the contour and use the contour to
        # compute the aspect ratio and coverage ratio of the bounding box
        # width to the width of the image
        (x, y, w, h) = cv2.boundingRect(c)
        ar = w / float(h)
        crWidth = w / float(gray.shape[1])
        # check to see if the aspect ratio and coverage width are within
        # acceptable criteria
        if ar > 5 and crWidth > 0.75:
            # pad the bounding box since we applied erosions and now need
            # to re-grow it
            pX = int((x + w) * 0.03)
            pY = int((y + h) * 0.03)
            (x, y) = (x - pX, y - pY)
            (w, h) = (w + (pX * 2), h + (pY * 2))

            # extract the ROI from the image and draw a bounding box
            # surrounding the MRZ
            roi = image[y:y + h, x:x + w].copy()
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            break

    cv2.imwrite('output_image_dataset/final_image.jpg', image)
    cv2.imwrite('output_image_dataset/output.jpg', roi)
    cv2.imshow('output', roi)
    cv2.waitKey(0)
