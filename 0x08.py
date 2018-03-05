'''
@author：KongWeiKun
@file: 0x08.py
@time: 18-3-5 下午4:56
@contact: 836242657@qq.com
'''
import bz2

un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
import bz2
bz2.BZ2Decompressor().decompress(un)
#b'huge'
bz2.BZ2Decompressor().decompress(pw)
#b'file'