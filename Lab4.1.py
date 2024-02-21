import cv2 as cv
import matplotlib.pyplot as plt

blur_img = cv.imread('Marisa.jpg', cv.IMREAD_COLOR)

blur_img_rgb = cv.cvtColor(blur_img, cv.COLOR_BGR2RGB)

sobelx = cv.Sobel(src=blur_img, ddepth=cv.CV_64F, dx=1, dy=0, ksize=5)
filtered_image_x = cv.convertScaleAbs(sobelx)

sobely = cv.Sobel(src=blur_img, ddepth=cv.CV_64F, dx=0, dy=1, ksize=5)
filtered_image_y = cv.convertScaleAbs(sobely)

sobelxy = cv.Sobel(src=blur_img, ddepth=cv.CV_64F, dx=1, dy=1, ksize=5)
filtered_image_xy = cv.convertScaleAbs(sobelxy)

plt.figure(figsize=(20, 20))

plt.subplot(221)
plt.imshow(blur_img_rgb)
plt.title('Original Image')
plt.axis("off")

plt.subplot(222)
plt.imshow(filtered_image_x, cmap='gray')
plt.title('Sobel X')
plt.axis("off")

plt.subplot(223)
plt.imshow(filtered_image_y, cmap='gray')
plt.title('Sobel Y')
plt.axis("off")

plt.subplot(224)
plt.imshow(filtered_image_xy, cmap='gray')
plt.title('Sobel XY')
plt.axis("off")

plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
