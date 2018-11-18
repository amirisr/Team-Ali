import cv2
import numpy as np
import time

def testLatency():
    cap = cv2.VideoCapture(0)
    start = time.time()
    ret, frame = cap.read()
    cap.release()
    print(time.time() - start)
    print(frame.shape)

def showVid():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture)
    cap.release()
    # cv2.destroyAllWindows()
    print(frame.shape)


if __name__ == "__main__":
    showVid()