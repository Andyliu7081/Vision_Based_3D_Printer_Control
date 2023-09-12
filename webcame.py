import cv2
import numpy as np
import glob
from numpy import array as matrix, arange

# Setup parameter, and loop max 30 times, bias in 0.001
criteria = (cv2.TERM_CRITERIA_EPS  + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
w = 6
h = 9

# Get corner positions
objp = np.zeros((w * h, 3), np.float32)
objp[:, :2] = np.mgrid[0:w, 0:h].T.reshape(-1, 2)

# storage 3D & 2D points
objpoints = []
imgpoints = []
record = []
# print('check1')

images = glob.glob('images_cli/*.jpg')

for fname in images:
    # print('check loop')
    img = cv2.imread(fname)
    # print('check2')
    cv2.imshow('img', img)
    # print('check3')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    size = gray.shape[::-1]
    ret, corners = cv2.findChessboardCorners(gray, (w, h), None)
    print(ret)

    if ret:
        record.append(fname)
        corners = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)

        objpoints.append(objp)
        imgpoints.append(corners)

        cv2.drawChessboardCorners(img, (w, h), corners, ret)
        cv2.imshow('findCorners', img)
        cv2.waitKey()
cv2.destroyAllWindows()

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, size, None, None)

print('ret'. ret)
print('inner', mtx)
print('distoration', dist)
print('rev', rvecs)
print('trans', tvecs)

img2 = cv2.imread('print_bed2.jpg')
h, w = img2.shape[:2]
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
dst = cv2.undistort(img2, mtx, dist, None, newcameramtx)

cv2.imshow('fin', dst)
cv2.imwrite('./fin.png', dst)
cv2.waitKey()
cv2.destroyAllWindows()

total_error = 0
for i in range(len(objpoints)):
    imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
    error = cv2.norm(imgpoints[i], imgpoints2, cv2.NORM_L2) / len(imgpoints2)
    total_error += error
print('total error', total_error / len(objpoints))