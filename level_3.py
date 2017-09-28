# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 08:51:19 2017

@author: Orion
"""
import re
mess2 = open('mess2.txt', 'r')

contenido = mess2.read()

string = "".join(re.findall("[a-zA-Z]",contenido))

for i in range(3,len(string)-7):
    if 97 <= ord(string[i]) <= 122:
        if (65 <= ord(string[i+1]) <= 90) and (65 <= ord(string[i+2]) <= 90) and (65 <= ord(string[i+3]) <= 90) and (string[i+4] == string[i+4].lower()): 
            if (65 <= ord(string[i-1]) <= 90) and (65 <= ord(string[i-2]) <= 90) and (65 <= ord(string[i-3]) <= 90) and (string[i-4] == string[i-4].lower()):          
                print(string[i-4] + string[i-3] + string[i-2] + string[i-1] +" "+ string[i] +" "+string[i+1] + string[i+2] + string[i+3] + string[i+4])                
    
