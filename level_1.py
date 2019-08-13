
string = "http://www.pythonchallenge.com/pc/def/map.html"
in_string =  "yzabcdefghijklmnopqrstuvwx"
out_string = "abcdefghijklmnopqrstuvwxyz"
trantab = str.maketrans(in_string, out_string)
print (string.translate(trantab))
