import numpy as np
import time
import cv2

#used for real-time web camera
vid = cv2.VideoCapture(0)

#to allow for camera to work
time.sleep(1)

background = 0

#used to process the video and frames it continues to read
while True:
    return_val, background = vid.read()
    if return_val == False:
        continue

    background = np.flip(background, axis=1)

#processes each frame
while vid.isOpened():
    return_val, image = vid.read()
    if not return_val:
        break

    image = np.flip(image, axis=1)

    #convert BGR to HSV (hue, saturation)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

   
    low_blue = np.array([100, 40, 40])  # lower bound of blue in HSV
    high_blue = np.array([140, 255, 255])  # upper bound of blue in HSV

    #changes the blue to white
    blue_mask = cv2.inRange(hsv, low_blue, high_blue)

    #removes some blobs and enlarges whiter areas
    blue_mask = cv2.morphologyEx(blue_mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    blue_mask = cv2.dilate(blue_mask, np.ones((3, 3), np.uint8), iterations=1)

    mask_inverse = cv2.bitwise_not(blue_mask)

    #combines the background with the foreground
    final1 = cv2.bitwise_and(background, background, mask=blue_mask)
    final2 = cv2.bitwise_and(image, image, mask=mask_inverse)

    final_output = cv2.addWeighted(final1, 1, final2, 1, 0)

    cv2.imshow("Cloak is On!", final_output)

    #use esc to leave the program
    k = cv2.waitKey(10)
    if k == 27:
        break

vid.release()
cv2.destroyAllWindows()
