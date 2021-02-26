import cv2

capture = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
outfile = cv2.VideoWriter('output.avi', fourcc, 25., (640, 480))

while(capture.isOpened()):
    ret, frame = capture.read()

    if ret:
        outfile.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break
