import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('Marisa.jpg')
blur = cv.blur(img, (5, 55))
Gblur = cv.GaussianBlur(img, (55, 5), 0)
Median = cv.medianBlur(img, 5)
Bblur = cv.bilateralFilter(img, 20, 200, 200)

font = cv.FONT_HERSHEY_TRIPLEX

cv.putText(blur, 'Averaging', (60, 15), font, 0.5, (255, 255, 255), 2)
cv.putText(Gblur, 'Gaussian Blur', (40, 15), font, 0.5, (255, 255, 255), 2)
cv.putText(img, 'Original', (65, 15), font, 0.5, (255, 255, 255), 2)
cv.putText(Median, 'Median', (75, 15), font, 0.5, (255, 255, 255), 2)
cv.putText(Bblur, 'Bilateral Filtering', (25, 15), font, 0.5, (255, 255, 255), 2)

plt.subplot(331), plt.imshow(blur)
plt.xticks([]), plt.yticks([])

plt.subplot(333), plt.imshow(Gblur)
plt.xticks([]), plt.yticks([])

plt.subplot(335), plt.imshow(img)
plt.xticks([]), plt.yticks([])

plt.subplot(337), plt.imshow(Median)
plt.xticks([]), plt.yticks([])

plt.subplot(339), plt.imshow(Bblur)
plt.xticks([]), plt.yticks([])
plt.show()