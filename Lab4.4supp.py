import cv2 as cv
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def apply_filters(frame):
    # Resize the frame to a smaller size
    small_frame = cv.resize(frame, (0, 0), fx=0.5, fy=0.5)

    # Sobel XY
    sobelxy = cv.Sobel(small_frame, cv.CV_64F, dx=1, dy=1, ksize=5)
    filtered_sobelxy = cv.convertScaleAbs(sobelxy)

    # Canny Edge
    edges_canny = cv.Canny(small_frame, 50, 150)

    # Laplacian Edge
    laplacian_edges = cv.Laplacian(small_frame, cv.CV_64F)
    laplacian_edges = cv.convertScaleAbs(laplacian_edges)

    return small_frame, filtered_sobelxy, edges_canny, laplacian_edges

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Set frames per second (fps) and calculate interval
fps = 30
interval = int(1000 / fps)

def update(frame):
    ret, frame = cap.read()
    small_frame, filtered_sobelxy, edges_canny, laplacian_edges = apply_filters(frame)

    # Adding titles to the frames
    frame_with_text = cv.putText(small_frame.copy(), 'Original Video', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv.LINE_AA)
    filtered_sobelxy_with_text = cv.putText(filtered_sobelxy.copy(), 'Sobel XY', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv.LINE_AA)
    edges_canny_with_text = cv.putText(edges_canny.copy(), 'Canny Edge', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv.LINE_AA)
    laplacian_edges_with_text = cv.putText(laplacian_edges.copy(), 'Laplacian Edge', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv.LINE_AA)

    # Plotting the original video with the original color
    axes[0, 0].imshow(cv.cvtColor(frame_with_text, cv.COLOR_BGR2RGB))
    axes[0, 0].axis("off")

    # Plotting Sobel XY
    axes[0, 1].imshow(filtered_sobelxy_with_text, cmap='gray')
    axes[0, 1].axis("off")

    # Plotting Canny Edge
    axes[1, 0].imshow(edges_canny_with_text, cmap='gray')
    axes[1, 0].axis("off")

    # Plotting Laplacian Edge
    axes[1, 1].imshow(laplacian_edges_with_text, cmap='gray')
    axes[1, 1].axis("off")

ani = FuncAnimation(fig, update, interval=interval, blit=False)
plt.show()

cap.release()
