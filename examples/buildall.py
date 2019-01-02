import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from os import walk
flist=[]
for (dirpath, dirnames, filenames) in walk("."):
    
    flist.extend(filenames)


flist.remove("buildall.py")
mlist=[x.split(".")[0] for x in flist ]
print flist
print mlist

myList = mlist
modules = map(__import__, myList)

