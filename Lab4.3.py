import cv2 as cv
import matplotlib.pyplot as plt


blur_img = cv.imread('Marisa.jpg', cv.IMREAD_GRAYSCALE)
blur_img_rgb = cv.cvtColor(blur_img, cv.COLOR_BGR2RGB)

laplacian_edges = cv.Laplacian(blur_img, cv.CV_64F)

plt.figure(figsize=(20, 20))

plt.subplot(221)
plt.imshow(blur_img_rgb)
plt.title('Original Image')
plt.axis("off")

plt.subplot(222)
plt.imshow(laplacian_edges, cmap='gray')
plt.title('Laplacian Edges')
plt.axis("off")

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
