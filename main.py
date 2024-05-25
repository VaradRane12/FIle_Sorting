import os,shutil
import re
path = r"D:\test_sorting/"
fl_lst = os.listdir(path)
y = []
for i in range(0,len(fl_lst)):
    if not os.path.isdir(path+fl_lst[i]):  #chekcing if the iterated file in a folder or a file appending only if its a file
        y.append(os.path.splitext(fl_lst[i])[1])

set(y)


for loop in range(0,len(y)):
    if not os.path.exists(path + y[loop]):
        os.makedirs(path + y[loop])



for i in y:
    for j in fl_lst:
        if i in j:
            try:
                shutil.move(path+j,path+i+"/"+j)
            except:
                continue

            