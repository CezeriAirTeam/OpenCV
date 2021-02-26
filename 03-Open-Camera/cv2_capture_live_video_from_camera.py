import cv2

capture = cv2.VideoCapture(2)

width, height = capture.get(3), capture.get(4)
print(width, height)


capture.set(cv2.CAP_PROP_FRAME_WIDTH, width * 2)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height * 2)

while(True):
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if cv2.waitKey(1) == ord('q'):
        break
