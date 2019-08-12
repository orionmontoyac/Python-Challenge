import pickle


pickle_in = open("/home/pdi/Python-Challenge/banner.p", "rb")
load = pickle.load(pickle_in)
for line in load:
    for camp in line:
        print(camp[0]*camp[1],end="")
    print()