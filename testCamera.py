import cv2
import numpy as np
import time


def testLatency(inp):
    cap = cv2.VideoCapture(inp)
    start = time.time()
    ret, frame = cap.read()
    cap.release()
    print(time.time() - start)
    print(frame.shape)


def showVid(inp):
    cap = cv2.VideoCapture(inp)
    while True:
        ret, frame = cap.read()
        cv2.imshow("frame " + str(inp), frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture)
    cap.release()
    cv2.destroyAllWindows()


def showMultiple(num):
    cap = [cv2.VideoCapture(i) for i in range(num)]
    while True:
        tmp = [x.read() for x in cap]
        ret = [x[0] for x in tmp]
        res = [x[1] for x in tmp]
        for x in res:
            cv2.imshow("frame: ", x)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture)
    for x in cap:
        x.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    testLatency(0)
    showMultiple(1)