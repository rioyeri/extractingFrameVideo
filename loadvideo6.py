import cv2
import numpy as np
import os

# Playing video from file:
cap = cv2.VideoCapture('fall-01-cam0.mp4')

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
ret = True
i = 0

while(ret):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if (currentFrame == 0) | (currentFrame % 25 == 0):
        print(currentFrame)

        # Saves image of the current frame in jpg file
        name = './data/frame' + str(i) + '.jpg'
        print ('Creating...' + name)
        cv2.imwrite(name, frame)

        i += 1
    # To stop duplicate images
    currentFrame += 1


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()