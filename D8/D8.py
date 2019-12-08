from collections import Counter
from matplotlib import pyplot as plt
from time import time
import numpy as np

t0 = time()
f = open(r'C:\Users\Panos\Google Drive\ECE\Python Files\Advent of Code 2019\D8\input.txt', 'r')
im_flattened = f.read()

im_wid = 25
im_hei = 6
img = np.full(im_wid*im_hei, 2)
i = len(im_flattened)

# P1
min_zeros = 99999
for i in range(0, len(im_flattened), im_wid*im_hei):
    layer = im_flattened[i:i+(im_wid*im_hei)]
    cnt = Counter(layer)
    if cnt['0'] < min_zeros:
        min_zeros = cnt['0']
        num = cnt['1']*cnt['2']
print(num)

# P2

for i in range(0, len(im_flattened), im_wid*im_hei):
    layer = im_flattened[i:i+(im_wid*im_hei)]
    for j in range(len(layer)):
        if layer[j] != '2' and img[j] == 2:
            img[j] = layer[j]

data = np.reshape(img, (6, 25))
plt.imshow(data, interpolation='nearest')
plt.show()
print(time() - t0)