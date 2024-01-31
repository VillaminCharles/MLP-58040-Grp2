# Python code to read image
import cv2

img = cv2.imread("Zuma.jpg", cv2.IMREAD_COLOR)

cv2.imshow("Zuma.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

q