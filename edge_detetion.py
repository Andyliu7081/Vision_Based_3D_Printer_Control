# ---------- simple image processing operators testing ----------
import cv2
import numpy as np
import matplotlib.pyplot as plt
 
# Read image
img = cv2.imread('image path')

# Image pre processing
img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gaussianBlur = cv2.GaussianBlur(grayImage, (3,3), 0)
ret, binary = cv2.threshold(gaussianBlur, 127, 255, cv2.THRESH_BINARY)
 
#Roberts
kernelx = np.array([[-1,0],[0,1]], dtype=int)
kernely = np.array([[0,-1],[1,0]], dtype=int)
x = cv2.filter2D(binary, cv2.CV_16S, kernelx)
y = cv2.filter2D(binary, cv2.CV_16S, kernely)
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)
Roberts = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
 
#Prewitt
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]], dtype=int)
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]], dtype=int)
x = cv2.filter2D(binary, cv2.CV_16S, kernelx)
y = cv2.filter2D(binary, cv2.CV_16S, kernely)
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)
Prewitt = cv2.addWeighted(absX,0.5,absY,0.5,0)
 
#Sobel
x = cv2.Sobel(binary, cv2.CV_16S, 1, 0)
y = cv2.Sobel(binary, cv2.CV_16S, 0, 1)
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)
Sobel = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
 
#Laplacian
dst = cv2.Laplacian(binary, cv2.CV_16S, ksize = 3)
Laplacian = cv2.convertScaleAbs(dst)

# plots
plt.subplot(231),plt.imshow(img_RGB),plt.title('pic'), plt.axis('off') #坐标轴关闭
plt.subplot(232),plt.imshow(Roberts, cmap=plt.cm.gray ),plt.title('Roberts'), plt.axis('off')
plt.subplot(233),plt.imshow(Prewitt, cmap=plt.cm.gray ),plt.title('Prewitt'), plt.axis('off')
plt.subplot(234),plt.imshow(Sobel, cmap=plt.cm.gray ),plt.title('Sobel'), plt.axis('off')
plt.subplot(235),plt.imshow(Laplacian, cmap=plt.cm.gray ),plt.title('Laplacian'), plt.axis('off')
 
plt.show()