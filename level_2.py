#level_2.py
import re
mess = open('mess.txt', 'r')

contenido = mess.read()

print ("".join(re.findall("[a-z]",contenido)))  