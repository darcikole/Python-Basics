import sqlite3

fileList = ('information.docx','Hello.txt','myImage.png',\
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')


conn = sqlite3.connect('py_103')
with conn:
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT)")
    
    conn.commit()
conn.close()

conn = sqlite3.connect('py_103')
with conn:
    c = conn.cursor()
              
for file in fileList:
    if file.endswith(".txt"):
        c.executemany("INSERT INTO tbl_files(col_fileName) VALUES(?)",(file))
        print(file)


        
    conn.commit()
    

