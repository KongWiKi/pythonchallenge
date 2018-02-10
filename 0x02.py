'''
@author：KongWeiKun
@file: 0x02.py
@time: 18-2-10 下午1:54
@contact: 836242657@qq.com
'''
import requests
import re
content = requests.get('http://www.pythonchallenge.com/pc/def/ocr.html').text
anwser = re.sub('\n|\t|\r','',content) #去除多余的空格空行 防止扰乱后续判断是否为字母
anwser = re.findall("find.*?<!--(.*?)-->",anwser) #匹配给出答案的内容
anwser = list(str(anwser)) #转化为列表
key = []
for x in anwser:
    if x.isalpha():
       key.append(x)
print("".join(key))