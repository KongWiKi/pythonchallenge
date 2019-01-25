"""
@author: kongwiki
@file:   0x12.py
@time:   19-1-25下午11:07
@contact: kongwiki@163.com
"""
data = open("./data/0x12/evil2.gfx", "rb").read()
print(len(data))

for i in range(5):
    open('./data/0x12/%d.jpg'%i, 'wb').write(data[i::5])

