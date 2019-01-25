"""
@author: kongwiki
@file:   0x11.py
@time:   19-1-25下午10:47
@contact: kongwiki@163.com
"""
from PIL import Image

image = Image.open('./data/cave.jpg')
(w, h) = image.size

even = Image.new('RGB', (w//2, h//2))
odd = Image.new('RGB', (w//2, h//2))

for i in range(w):
    for j in range(h):
        p = image.getpixel((i, j))
        if (i+j)/2 == 1:
            odd.putpixel((i//2, j//2), p)
        else:
            even.putpixel((i//2, j//2), p)

even.save('./data/0x11/even.jpg')
odd.save('./data/0x11/odd.jpg')
