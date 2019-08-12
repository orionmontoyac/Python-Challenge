# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 23:05:32 2017

@author: Orion
"""
from urllib.request import urlopen
import re

uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

num = "63579"
#num = str(16044/2)

pattern = re.compile("and the next nothing is (\d+)")

while True:
    pharse = urlopen(uri + num).read().decode('utf-8')
    print(pharse)
    match = pattern.search(pharse)
    if match == None:
        break
    num = re.findall('[0-9]{1,10}',pharse)[0]
