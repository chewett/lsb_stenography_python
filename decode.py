import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img.png')
b,g,r = cv2.split(img) #get colour parts


def get_lsb(a):
    new_img = []
    count = 7
    accum_val = 0
    for row in a:
        for col in row:
            pixel_val = col
            accum_val += (pixel_val % 2) * (2 ** count) #get the LSB
            count -= 1

            if count == -1:
                new_img.append(accum_val)
                count = 7
                accum_val = 0

    pix_count = 0
    reformatted_img = []
    row = []
    for pix in new_img:
        pix_count += 1
        row.append(pix)

        if pix_count == 300:
            pix_count = 0
            reformatted_img.append(row)
            row = []

    return reformatted_img


print len(b)
print len(b[0])

new_b = np.asarray(get_lsb(b))
new_g = np.asarray(get_lsb(g))
new_r = np.asarray(get_lsb(r))

img2 = cv2.merge((new_b,new_g,new_r))
print img2

cv2.imwrite("decoded.png", img2)

img_show = True

if img_show is True:
    plt.subplot(121),plt.imshow(img),plt.title('ORIGINAL')
    plt.subplot(122),plt.imshow(img2),plt.title('HIDDEN')
    plt.show()
