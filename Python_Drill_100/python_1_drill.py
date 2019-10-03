
import os
import time

path = "/Applications/GitHub/Python Basics/Python_Drill_100/Drill Files"

myDir = os.listdir(path)

for file in myDir:
    print(file)

for file in myDir:
    if file.endswith(".PNG"):
        print(os.path.join(path,file))
    else:
        continue

for file in myDir:
    if file.endswith(".txt"):
        theFile = os.path.join(path,file)
        ModTime = os.path.getmtime(theFile)
        realTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(ModTime))
        print(file,realTime)
    else:
        continue
