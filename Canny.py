import cv2

fileName = "zebra.jpg"

image = cv2.imread("images/" + fileName, cv2.IMREAD_GRAYSCALE)
edges = cv2.Canny(image, 220, 250)

cv2.imshow("CV2 Canny Edge Detection", edges)
cv2.waitKey(0)

cv2.destroyAllWindows()
