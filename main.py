import os,shutil
import re
path = r"D:\test_sorting/"
full_name_ext = {}
y = []
fl_lst = os.listdir(path)
for i in range(0,len(fl_lst)):
    if not os.path.isdir(path+fl_lst[i]):  #chekcing if the iterated file in a folder or a file appending only if its a file
        full_name_ext[i] = [fl_lst[i],os.path.splitext(fl_lst[i])[0],os.path.splitext(fl_lst[i])[1]]
        y.append(os.path.splitext(fl_lst[i])[1])
y = set(y)


i = 0
file =  open("Text_sort.txt")
ext_lst = file.readlines()
while i<len(ext_lst):
    if (i%2 == 0):
        for j in range(1,len(full_name_ext)):
#             print(full_name_ext[j][1])
            if(ext_lst[i].replace("\n","") in full_name_ext[j][1]):
                try:
                    print("intial list",full_name_ext[j][0])
                    print("path:",ext_lst[i+1])
                    print(path+full_name_ext[j][0])
                    shutil.move(path+full_name_ext[j][0],ext_lst[i+1].replace("\n",""))
                except:
                    i+=1
                    continue
                
        i+=1
    else:
        i+=1
        continue


for loop in range(0,len(y)):
    if not os.path.exists(path + y[loop]):
        os.makedirs(path + y[loop])



for i in y:
    for j in full_name_ext.values():
        if i in j[0]:
            try:
                shutil.move(path+j[0],path+i+"/"+j[0])
            except:
                continue

            
           