%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import cv2
from scipy import ndimage

#Read image from path
img_100 = cv2.imread("exposure-100.png")
img_4100 = cv2.imread("exposure-4100.png")
img_8100 = cv2.imread("exposure-8100.png")
img_12100 = cv2.imread("exposure-12100.png")
img_16100 = cv2.imread("exposure-16100.png")
img_20100 = cv2.imread("exposure-20100.png")
dim_100 = img_100[:, :, 0]
dim_4100 = img_4100[:, :, 0]
dim_8100 = img_8100[:, :, 0]
dim_12100 = img_12100[:, :, 0]
dim_16100 = img_16100[:, :, 0]
dim_20100 = img_20100[:, :, 0]

rows, cols = 1440, 2560
# Identify the window size of variance to be determined
w_rows, w_cols = 20, 20
# This function calculate the variance as dispersion of the image
def cal_variance(img):
    w_mean = ndimage.uniform_filter(img, (w_rows, w_cols))
    w_sqr_mean = ndimage.uniform_filter(img**2, (w_rows, w_cols))
    w_var = w_sqr_mean - w_mean**2
    var = np.average(w_var)
    return var

#Figure out the variance for each image, we can figure out that the best image is exposure-16100
var100 = cal_variance(dim_100)
var4100 = cal_variance(dim_4100)
var8100 = cal_variance(dim_8100)
var12100 = cal_variance(dim_12100)
var16100 = cal_variance(dim_16100)
var20100 = cal_variance(dim_20100)
print(var100)
print(var4100)
print(var8100)
print(var12100)
print(var16100)
print(var20100)