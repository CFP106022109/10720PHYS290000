# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt

fp = open("Alice.txt","r",encoding = "UTF-8")

line = fp.readline()

my_dict = {}

while line:
    s = line.split()
    for i in s:
        if i not in my_dict:
            my_dict[i] = 1 
            
        else:
            my_dict[i] = my_dict[i] + 1

    line = fp.readline()            

fp.close()

num = []

for key in my_dict:
    num.append(my_dict[key])

print(len(num))

num.sort()
num.reverse()
print(num)

plt.loglog(range(len(num)),num)
plt.xlabel("Rank of the word")
plt.ylabel("Number of the occurance")
plt.show()




