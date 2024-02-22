import cv2 as cv
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def apply_filters(frame):
    small_frame = cv.resize(frame, (0, 0), fx=0.5, fy=0.5)
    sobelxy = cv.Sobel(small_frame, cv.CV_64F, dx=1, dy=1, ksize=5)
    filtered_sobelxy = cv.convertScaleAbs(sobelxy)
    edges_canny = cv.Canny(small_frame, 50, 150)
    laplacian_edges = cv.Laplacian(small_frame, cv.CV_64F)
    laplacian_edges = cv.convertScaleAbs(laplacian_edges)
    return small_frame, filtered_sobelxy, edges_canny, laplacian_edges


cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

filter_names = ['Original Video', 'Sobel XY', 'Canny Edge', 'Laplacian Edge']

fps = 1000
interval = int(1000 / fps)


def update(frame):
    ret, frame = cap.read()
    processed_frames = apply_filters(frame)

    for ax, img, filter_name in zip(axes.flat, processed_frames, filter_names):
        img_with_text = cv.putText(img.copy(), filter_name, (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1,
                                   cv.LINE_AA)

        # Check the number of channels before conversion
        if img_with_text.shape[-1] == 1:
            ax.imshow(img_with_text, cmap='gray')
        else:
            ax.imshow(cv.cvtColor(img_with_text, cv.COLOR_BGR2RGB), cmap='gray')

        ax.axis("off")


ani = FuncAnimation(fig, update, interval=interval, blit=False)
plt.show()

cap.release()
