import os,shutil
import re
import watchdog.events
import watchdog.observers
import time


global path 
path = r"D:\test_sorting/"
full_name_ext = {}
y = []


class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        # Set the patterns for PatternMatchingEventHandler
        watchdog.events.PatternMatchingEventHandler.__init__(self,ignore_directories=True, case_sensitive=False)

    def on_created(self, event):
        named_file_check(full_name_ext)
        dir_path_sort(y,full_name_ext)

#     def on_modified(self, event):
#         print("Watchdog received modified event - % s." % event.src_path)
#         # Event is modified, you can process it now
    def on_moved(self,event):
        print("Moved %s"%event.src_path)
    def on_deleted(self,event):
        print("deleted %s"%event.src_path)
def named_file_check(full_name_ext):
    i = 0
    file =  open("file_types.txt")
    ext_lst = file.readlines()
    while i<len(ext_lst):
        if (i%2 == 0):
            for j in range(1,len(full_name_ext)):
                if(ext_lst[i].replace("\n","") in full_name_ext[j][1]):
                    try:
                        if os.path.exists(ext_lst[i+1].replace("\n","")+"/"+full_name_ext[j][0]):
                            print("the file already exists in the destination folder")
                            continue
                        shutil.move(path+full_name_ext[j][0],ext_lst[i+1].replace("\n",""))        
                    except :
                        i+=1
                        continue      
            i+=1
        
        else:
            i+=1
            continue
def dir_path_sort(y,full_name_ext):
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

fl_lst = os.listdir(path)


for i in range(0,len(fl_lst)):
    if not os.path.isdir(path+fl_lst[i]):  #chekcing if the iterated file in a folder or a file appending only if its a file
        full_name_ext[i] = [fl_lst[i],os.path.splitext(fl_lst[i])[0],os.path.splitext(fl_lst[i])[1]]
        y.append(os.path.splitext(fl_lst[i])[1])
y = set(y)




if __name__ == "__main__":
    src_path = r"D:\test_sorting/"
    event_handler = Handler()
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

            
           