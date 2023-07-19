import cv2
from PIL import Image, ImageOps, ImageFilter
import matplotlib.pyplot as plt
import numpy as np
from transitions import Machine

def camera():
    cap = cv2.VideoCapture(0)
    num = 1
    while(cap.isOpened()): # check camera status
        ret_flag,Vshow = cap.read() # get img
        cv2.imshow("Capture_Test",Vshow) # display img
        k = cv2.waitKey(1) & 0xFF
        if k == ord('s'): # press S to save
            cv2.imwrite('saved image'+str(num)+".jpg",Vshow) #route
            print("success to save "+str(num)+".jpg")
            print("-------------------------")
            num += 1
        elif k == ord(' '): #press ' ' to exit
            break

    cap.release() # release storage
    cv2.destroyAllWindows() # exit and close all window

img = "/Users/liuhaotian/Desktop/Camera_cali/saved image1.jpg"
def grayscale(img):
    src = cv2.imread(img)
    cv2.imshow("src", src)
    
    plt.hist(src.ravel(), 256)
    plt.show()
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# camera()
grayscale(img)
