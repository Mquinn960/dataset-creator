import cv2, sys, os
from time import sleep

label = input("Please enter training class label: ").upper()
mode = input("Training Mode [manual/auto]: ")

if mode != "manual" and mode != "auto":
    print("Training mode unrecognised")
    sys.exit()

if mode == "auto":
    images = input("Number of images to record per class: ")
    delay = input("Delay before recording (seconds): ")

path = input("If folder required specify name otherwise leave blank: ")

if path != "":
    if os.path.exists(path) == False:
        os.mkdir(path)

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

if mode == "manual":
    while True:
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = path + "/" + label + "_1_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
elif mode == "auto":
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

        img_name = path + "/" + label + "_1_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()