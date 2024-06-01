import os,shutil
import re
path = r"D:\test_sorting/"
full_name_ext = {}
fl_lst = os.listdir(path)
for i in range(0,len(fl_lst)):
    if not os.path.isdir(path+fl_lst[i]):  #chekcing if the iterated file in a folder or a file appending only if its a file
        full_name_ext[fl_lst[i]] = [os.path.splitext(fl_lst[i])[0],os.path.splitext(fl_lst[i])[1]]

i = 0
file =  open("file_types.txt")
ext_lst = file.readlines()
while i<len(ext_lst):
    if (i%2 == 0):
        for j in range(0,len(names)):
            if(ext_lst[i].replace("\n","") in names[j]):
                try:
                    print("intial list",fl_lst[j+1])
                    print("path:",ext_lst[i+1])
                    print(path+fl_lst[j+1])
                    shutil.move(path+fl_lst[j+1],ext_lst[i+1].replace("\n",""))
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
    for j in fl_lst:
        if i in j:
            try:
                shutil.move(path+j,path+i+"/"+j)
            except:
                continue

            
            #CHANGE EVERYTHING TO THE NEW DICTIONARY