#level_2.py
import re
mess = open('/home/pdi/Python-Challenge/Mess.txt', 'r')

contenido = mess.read()

print ("".join(re.findall("[a-z]",contenido)))  