import cv2 as cv
import numpy as np
import math
def generate_phase_image(width=1920,high=1080,f=16,A=128,B=127):
    for k in range(4):
        img = np.zeros((high,width),np.uint8)
        for i in range(high):
            for j in range(width):
                phase = A + B*math.cos(2*math.pi*(f*j/width+k/4))
                img[i,j] = phase;
        img_num = str(k)
        filename = 'phase_image_' + img_num + '.jpeg'
        cv.imwrite(filename,img)
    return
if __name__ == '__main__':
    generate_phase_image()