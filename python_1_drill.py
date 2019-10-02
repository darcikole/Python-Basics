
import os
import time

path = "/Applications/GitHub/Python Basics/Python_Drill_100"

fName = "SeahawksGame.PNG"

myDir = os.listdir(path)

for file in myDir:
    print(file)


newPath = os.path.join(path, fName)
print(newPath)

modificationTime = os.path.getmtime(path)
realTime = time.ctime(modificationTime)


for file in myDir:
    if file.endswith(".txt"):
        print(file,realTime)
        
    










