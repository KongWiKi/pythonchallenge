'''
@author：KongWeiKun
@file: 0x01.py
@time: 18-2-10 下午1:54
@contact: 836242657@qq.com
'''
intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"
str_trantab = str.maketrans(intab, outtab)

test_str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
#提示
print(test_str.translate(str_trantab))
#答案
m ,a ,p = ord('m'),ord('a'),ord('p')
print(chr(m+2),chr(a+2),chr(p+2))
