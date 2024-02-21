import cv2 as cv
import matplotlib.pyplot as plt

blur_img = cv.imread('Marisa.jpg', cv.IMREAD_GRAYSCALE)


edges = cv.Canny(blur_img, 50, 150)


plt.figure(figsize=(20, 20))


plt.subplot(221)
plt.imshow(blur_img, cmap='gray')
plt.title('Original Image')
plt.axis("off")


plt.subplot(222)
plt.imshow(edges, cmap='gray')
plt.title('Canny Edges')
plt.axis("off")

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()