# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 08:51:19 2017
@author: Orion
"""
import re
mess2 = open('/home/pdi/Python-Challenge/Mess2.txt', 'r')

contenido = mess2.read()

string = re.findall("[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}", contenido)
for i in string:
    print(i[4], end='')
print()
