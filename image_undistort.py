import cv2 as cv
import numpy as np
from pypylon import pylon
import image_capture as ic
IntrinsicMatrix = np.array([[3723.59625012744,-0.194358609991441,2045.90415334673],[0,3727.69735130794,1512.19338984103],[0,0,1]])
distCoeffs = np.float32([-0.0578544915703481,0.184339661415544,0.00104091470876287,-0.000266419879909606,-0.757716875809038])

def undistort_image(result,num_img):
    r"""相机去畸变程序,result是相机捕获到的图像数据 num_img是对应图像的序号"""
    converter = pylon.ImageFormatConverter()
    image = converter.Convert(result)
    img = image.GetArray()
    dst_img = cv.undistort(img,IntrinsicMatrix,distCoeffs)
    filename = 'saved_undistort_img_' + num_img + '.jpeg'
    cv.imwrite(filename,dst_img)

