import cv2 as cv


def capture_and_save():
    cap = cv.VideoCapture(0)
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter('Supp.mp4v', fourcc, 30.0, (640, 480))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        cv.imshow('frame', frame)
        out.write(frame)
        if cv.waitKey(1) == ord('q'):
            break

    cap.release()
    out.release()
    cv.destroyAllWindows()


def play_saved_video():
    play_video_file('Supp.mp4v')


def play_video_file(file_path):
    cap = cv.VideoCapture(file_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        cv.imshow('frame', frame)
        if cv.waitKey(30) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    while True:
        print("Select an option:")
        print("1. Capture and Save Video")
        print("2. Play Saved Video")
        print("Press 'q' to exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            capture_and_save()
        elif choice == '2':
            play_saved_video()
        elif choice.lower() == 'q':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 'q'.")

        choice = input("Enter your choice: ")

        if choice == '1':
            capture_and_save()
        elif choice == '2':
            play_saved_video()
        elif choice.lower() == 'q':
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 'q'.")
