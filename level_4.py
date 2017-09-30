# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 23:05:32 2017

@author: Orion
"""
import re
import urllib
link = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
number = '12345'
for i in range(0,400):
    url = urllib.request.urlopen(link+number)
    msg = url.read()
    number = ''.join(re.findall('[1-9]',msg.decode("utf-8")))
    print(str(i) +': '+msg.decode("utf-8"))