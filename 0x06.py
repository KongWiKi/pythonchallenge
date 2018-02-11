'''
@author：KongWeiKun
@file: 0x06.py
@time: 18-2-11 下午1:19
@contact: 836242657@qq.com
'''
import re
import glob as gb
import os
import zipfile
nextNothing ='90052'
basepath = './data/channel/*'
toalpath = gb.glob(basepath)#获取所有文件路径
file = zipfile.ZipFile('./data/channel.zip','r')
print(file)
for name in file.namelist():
    line = str(file.read("%s.txt" %nextNothing))
    m = re.search('Next nothing is ([0-9]+)', line)
    print (file.getinfo("%s.txt" % nextNothing).comment.decode("utf-8"), end=" ")
    nextNothing = m.group(1)


##此函数并无太多意义 只是回顾一下之前的知识
i =0
def getName():
    global i
    fileNumber = []
    for path in toalpath:
        i += 1
        _, filename = os.path.split(path)
        number = re.search("\d+",filename).group(0)
        fileNumber.append(number)
    return fileNumber,i



