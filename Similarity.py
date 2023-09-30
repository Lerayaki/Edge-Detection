import cv2
import numpy as np


def blurr(image, windowRadius=2):
    (height, width, _) = image.shape

    output = np.zeros((height, width, 3), np.uint8)

    mask = np.ones((windowRadius * 2 + 1, windowRadius * 2 + 1), dtype=bool)
    mask[windowRadius, windowRadius] = False

    for i in range(0, height):
        for j in range(0, width):
            output[i, j] = np.mean(
                image[
                    max(0, i - windowRadius) : min(height, i + windowRadius),
                    max(0, j - windowRadius) : min(width, j + windowRadius),
                ],
                axis=(0, 1),
            )

    return output


def similarity(image, windowRadius=2, threshold=0.15):
    (height, width, _) = image.shape

    output = np.zeros((height, width, 3), np.uint8)

    mask = np.ones((windowRadius * 2 + 1, windowRadius * 2 + 1), dtype=bool)
    mask[windowRadius, windowRadius] = False

    for i in range(0, height):
        for j in range(0, width):
            simil = (
                np.mean(
                    image[
                        max(0, i - windowRadius) : min(height, i + windowRadius),
                        max(0, j - windowRadius) : min(width, j + windowRadius),
                    ],
                    axis=(0, 1),
                )
                - image[i, j]
            )
            if np.mean(simil) >= threshold * 255:
                output[i, j] = [255, 255, 255]

    return output


image = cv2.imread("images/zebra.jpg")
borders = similarity(image, 3, 0.1)
stack = np.concatenate((image, borders))

cv2.imshow("zebra", stack)
cv2.waitKey(0)

cv2.destroyAllWindows()
