import cv2 as cv
import numpy as np

firstImage = cv.imread('1.png')
secondImage = cv.imread('2.png')

resizeFirstImage = cv.resize(firstImage, None, fx=0.3, fy=0.3)
image = resizeFirstImage
resizeSecondImage = cv.resize(secondImage, None, fx=0.3, fy=0.3)
numpy_horizontal_concat = np.concatenate((image, resizeSecondImage), axis=1)
winName = 'image'
cv.namedWindow(winName)
cv.moveWindow(winName, 40, 30)
cv.imshow(winName, numpy_horizontal_concat)
cv.waitKey()

# threshold = 20

imageShape1 = resizeFirstImage.shape
imageShape2 = resizeSecondImage.shape

h1 = imageShape1[0]
w1 = imageShape1[1]

h2 = imageShape2[0]
w2 = imageShape2[1]

if h1 != h2 or w2 != w2:
    print("Size of images are different")
else:
    for y in range(0, h1):
        for x in range(0, w1):
            if resizeFirstImage[y, x][0] != resizeSecondImage[y, x][0] or \
                    resizeFirstImage[y, x][1] != resizeSecondImage[y, x][1] or \
                    resizeFirstImage[y, x][2] != resizeSecondImage[y, x][2]:
                    # abs(resizeFirstImage[y, x][0] - resizeSecondImage[y, x][0]) > threshold or \
                    # abs(resizeFirstImage[y, x][1] != resizeSecondImage[y, x][1]) > threshold or \
                    # abs(resizeFirstImage[y, x][2] != resizeSecondImage[y, x][2]) > threshold:
                resizeSecondImage[y, x][0] = 0
                resizeSecondImage[y, x][1] = 0
                resizeSecondImage[y, x][2] = 255

winName = 'result'
cv.namedWindow(winName)
cv.moveWindow(winName, 40, 30)
cv.imshow(winName, resizeSecondImage)
cv.waitKey()
cv.destroyAllWindows()




































