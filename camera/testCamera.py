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
            cv2.imwrite("outbmp.bmp", frame)
            cv2.waitKey(0)
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


def imageDemo():
    lst = np.array([[[0, 3 ** 14, 2**16]] * 640] * 480)
    for i in range(lst.shape[0]):
        for j in range(lst.shape[1]):
            for k in range(lst.shape[2]):
                lst[i][j][k] = round(2**17 * (i/480)**2 * (k+1)/3, 0)
    print(lst.shape)
    while True:
        cv2.imshow("frame: ", lst)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    im = cv2.imread("copy.bmp", cv2.COLOR_BGR2RGB)
    print(im[145, 415])
    # showVid(0)