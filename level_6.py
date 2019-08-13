import os, re, zipfile
next_file = "90052"
zip_file = zipfile.ZipFile("/home/pdi/Python-Challenge/channel.zip")
pattern = re.compile("Next nothing is (\d+)")
comments = [] 
while True:
    pharse = open("/home/pdi/Python-Challenge/channel/" + next_file + ".txt","r").read()
    comments.append(zip_file.getinfo(next_file + ".txt").comment.decode("utf-8"))
    print(pharse)
    match = pattern.search(pharse)
    if match == None:
        break
    next_file = re.findall('[0-9]{1,10}',pharse)[0]

print("".join(comments))