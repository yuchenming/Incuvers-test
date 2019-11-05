%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import cv2

#Read image from path
img = cv2.imread("exposure-4100.png")
dim =img[:, :, 0]
print(dim.shape)
plt.imshow(dim)

# Function 1: The image could be normilized to exposure
def normalize(img):
    minNum = img.min()
    maxNum = img.max()
    return img - minNum * 255 / (maxNum - minNum)

img_new = normalize(img)
plt.imshow(img_new)
cv2.imwrite('exposure-4100-new.png', img_new)

# Function 2: Increase the exposure by adding value to valid pixel
dim_copy = dim
for i in range(1440):
    for j in range(2560):
        if((dim_copy[i,j] + 80) > 255):
            dim_copy[i,j] = 255
        else:
            dim_copy[i,j]
plt.imshow(dim_copy)
cv2.imwrite('exposure-4100-new2.png', dim_copy)