import cv2
import os
import time


cam = cv2.VideoCapture(0)
path = '/assets/'
cv2.namedWindow("Pythonnnnnnnnnnnnnn")

def doc():
    img_counter = 0
    while True:
        ret, frame = cam.read()
        if not ret:
            print("ERROR")
            break

        cv2.imshow("test", frame)
        k = cv2.waitKey(1)
        if k % 256 == 27:
            print("Escape hit")
            break

        elif k % 256 == 49:
            img_name = "doc.jpg".format(img_counter)
            cv2.imwrite(os.path.join(path, img_name), frame)
            print("Photo taken. Saved as {}".format(img_name))
            img_counter += 1

        elif k % 256 == 50:
            ret, frame = cam.read()
            img_name = "face.jpg".format(img_counter)
            cv2.imwrite(os.path.join(path, img_name), frame)
            print("Second photo taken. Saved as {}".format(img_name))
            img_counter += 1

    cam.release()

