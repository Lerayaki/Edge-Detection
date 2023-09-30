import cv2
import numpy as np


def MeanBlur(image, kernelSize=5):
    (h, w, c) = image.shape
    output = np.zeros_like(image)

    kerRad = kernelSize // 2

    for i in range(0, h):
        for j in range(0, w):
            window = image[
                max(0, i - kerRad) : min(h, i + kerRad),
                max(0, j - kerRad) : min(w, j + kerRad),
            ]
            if c > 1:
                output[i][j] = np.mean(window, axis=(0, 1))
            else:
                output[i][j] = np.mean(window)
    return output


image = cv2.imread("images/zebra-s.jpg")
mean = MeanBlur(image)
stack = np.concatenate((image, mean))
cv2.imshow("Mean Blurr", stack)
cv2.waitKey(0)

cv2.destroyAllWindows()
