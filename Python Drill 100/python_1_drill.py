
import os
import time

path = "/Applications/GitHub/Python Basics/Python Drill 100"

fName = "SeahawksGame.PNG"

txt1Path = "/Applications/GitHub/Python Basics/Python Drill 100/file 1.txt"
txt2Path = "/Applications/GitHub/Python Basics/Python Drill 100/file 2.txt"

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
        
    










