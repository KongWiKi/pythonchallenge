'''
@author：KongWeiKun
@file: 0x03.py
@time: 18-2-10 下午5:07
@contact: 836242657@qq.com
'''
import re
import requests

content = requests.get('http://www.pythonchallenge.com/pc/def/equality.html').text
anwser = re.sub('\n','',content)
pattern = re.compile('<!--(.*?)-->',re.S)
anwser = re.findall(pattern,str(anwser))
key = re.findall('[a-z]+[A-Z]{3}([a-z])[A-Z]{3}[a-z]+',str(anwser))
print("".join(key))