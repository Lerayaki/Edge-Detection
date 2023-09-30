import cv2
import numpy as np
import os


def EdgeFilter(image, threshold=0.1):
    output = np.zeros_like(image)
    output[np.mean(image, axis=2) > threshold * 255] = (255, 255, 255)
    return output


def EdgeOverlay(image, edges, color=(0, 0, 255)):
    output = np.array(image, copy=True)
    output[np.mean(edges, axis=2) > 0] = color
    return output


def LabelImage(image, label, color=(255, 255, 255)):
    position = (10, 25)
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 0.6
    thickness = 1
    return cv2.putText(
        image, label, position, font, fontScale, color, thickness, cv2.LINE_AA
    )


def LinearScaling(image):
    (h, w, c) = image.shape

    max = np.max(image, axis=(0, 1))
    min = np.min(image, axis=(0, 1))

    output = np.array(255 * ((image - min) / (max - min)), dtype="uint8")

    return output


def Difference(image1, image2):
    return np.array(abs(np.array(image1, dtype="int16") - image2), dtype="uint8")


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
            output[i][j] = np.mean(window, axis=(0, 1))
    return output


fileName = "zebra.jpg"

image = cv2.imread("images/" + fileName)
mean = MeanBlur(image, 5)

diff = Difference(image, mean)
scaled = LinearScaling(diff)

edgesLow = EdgeFilter(scaled, 0.15)
overlayLow = EdgeOverlay(image, edgesLow, color=(0, 0, 255))

edgesHigh = EdgeFilter(scaled, 0.23)
overlayHigh = EdgeOverlay(image, edgesHigh, color=(0, 255, 0))

doubleBlurr = EdgeFilter(LinearScaling(Difference(MeanBlur(scaled, 3), scaled)), 0.2)
doubleOverlay = EdgeOverlay(image, doubleBlurr)

loss = edgesLow - doubleBlurr

stack = np.concatenate(
    (
        np.concatenate(
            (
                LabelImage(image, "Original"),
                LabelImage(mean, "Mean Blur"),
                LabelImage(diff, "Difference"),
            ),
            axis=1,
        ),
        np.concatenate(
            (
                LabelImage(scaled, "Linear Scaled Diff."),
                LabelImage(overlayLow, "Low Threshold Filtered Edge Overlay"),
                LabelImage(overlayHigh, "Higher Threshold Filtered Edge Overlay"),
            ),
            axis=1,
        ),
        np.concatenate(
            (
                LabelImage(doubleBlurr, "Double Blurr Noise Reduction"),
                LabelImage(doubleOverlay, "Double Blurr Overlay"),
                LabelImage(loss, "Edge Loss on Second Blurr (vs Low Threshold)"),
            ),
            axis=1,
        ),
    )
)

cv2.imshow("Mean Blurr Edge Detection", stack)
cv2.waitKey(0)

cv2.destroyAllWindows()

cv2.imwrite("images/generated/Mean-" + fileName + "/", stack)

if not os.path.exists("images/generated/Mean-" + fileName):
    os.makedirs("images/generated/Mean-" + fileName)
cv2.imwrite("images/generated/Mean-zebra/blurred.jpg", mean)
cv2.imwrite("images/generated/Mean-zebra/diff.jpg", diff)
cv2.imwrite("images/generated/Mean-zebra/scaled.jpg", scaled)
cv2.imwrite("images/generated/Mean-zebra/edges.jpg", edgesHigh)
cv2.imwrite("images/generated/Mean-zebra/edgesLow.jpg", edgesLow)
cv2.imwrite("images/generated/Mean-zebra/overlay.jpg", overlayHigh)
cv2.imwrite("images/generated/Mean-zebra/doubleBlurr.jpg", doubleBlurr)
cv2.imwrite("images/generated/Mean-zebra/doubleOverlay.jpg", doubleOverlay)
cv2.imwrite("images/generated/Mean-zebra/doubleLoss.jpg", loss)
