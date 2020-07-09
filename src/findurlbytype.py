import os
filename = "webapplog.txt"
days_file = open(filename,'r')
data =[]
for l in days_file.readlines():
    temp = l.split("- -")
    data.append(temp[0])

dict = {}
for i in data:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] = dict[i]+1
print(dict)
