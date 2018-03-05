'''
@author：KongWeiKun
@file: 0x10.py
@time: 18-3-5 下午7:46
@contact: 836242657@qq.com
'''


def anwser():
    a = ["1", "11", "21", "1211", "111221"]
    while len(a) != 31:
        c, n = 0, 0
        r = []
        for i in a[-1]:
            if i != n:
                if c != 0:
                    r.append("%d%s" % (c, n))
                n = i
                c = 1
            else:
                c += 1
        r.append("%d%s" % (c, n))
        x = "".join(r)
        a.append(x)
    return len(a[30])

print(anwser())



