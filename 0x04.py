'''
@author：KongWeiKun
@file: 0x04.py
@time: 18-2-10 下午5:41
@contact: 836242657@qq.com
'''
import requests,re

number = re.compile("(\d+)")
rs = "12345"

def anwser():
    global rs
    for i in range(401):
        source = requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+rs).text
        if re.findall(number,source):
            if len(re.findall(number,source)) == 2:
                rs = re.findall(number, source)
                content = requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+rs[0]).text
                if content.find("You've been misleaded to here.") != -1:
                    print("不是数字{}是数字{}".format(rs[0],rs[1]))
                    rs = rs[1]
            else:
                rs = re.search(number,source).group(1)
                print("数字是{} 为第{}个".format(rs,i))
        else:
            if re.findall("Divide by two and keep going.",source):
            # if source.find("Divide by two and keep going.") != -1: 没有该字符串返回为-1
                print(source)
                rs = str(int(rs)/2)
            else:
                print(i,source)
                break

if __name__ == '__main__':
    anwser()



