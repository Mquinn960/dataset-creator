import cv2, sys, os
from time import sleep

images = 100
delay = 10
label = "A"

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

ret, frame = cam.read()
cv2.imshow("test", frame)
sleep(int(delay))
while True and img_counter != int(images):
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break

    img_name = label + "_1_{}.png".format(img_counter)
    cv2.imwrite(img_name, frame)
    print("{} written!".format(img_name))
    img_counter += 1

cam.release()

cv2.destroyAllWindows()