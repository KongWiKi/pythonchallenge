'''
@author：KongWeiKun
@file: 0x05.py
@time: 18-2-10 下午8:02
@contact: 836242657@qq.com
'''
import pickle
path = './data/banner.p'
# print(pickle.load(open("./data/banner.p","rb")))
def five():
    f = open(path, "rb")
    reader = pickle.load(f)
    f.close()
    for list in reader:
        print(list)
        # for x in list:
        #     print(x)
        # print(''.join(x[0]*x[1] for x in list))
five()
