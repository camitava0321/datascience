# -*- coding: utf-8 -*-
#Create the list of files from a specified folder
#output - on screen and a file
#file output format filename, file_location

import os
import collections as coll
from operator import attrgetter
import string

#array to hold the file namedtuples
fileRecords = []
#namedtuple to hold a file details
FileRecord = coll.namedtuple('FileRecord','name, path')

#Follow the root folder recursively
for root, dirs, files in os.walk("F:\\Bengali\\"):
    path = root.split(os.sep)
    for file in files:
        #create the namedtuple
        f = FileRecord (file,path)
        #append the namedtuple in array
        fileRecords.append(f);

#sort the array for the filenames a->z
sorted_f = sorted(fileRecords, key=lambda t: t.name.lower()) #attrgetter('name').lower())
fileO = open ('d:\\bengali\\booklist.csv','w+')

#traverse the array
for f in sorted_f:
    pathString = '\\'.join(f.path)
    name = string.replace(f.name,',','-')
    if ".jpg" in name.lower() :
        continue
    if ".gif" in name.lower() :
        continue
    if ".bmp" in name.lower() :
        continue
    if "thumbs.db" in name.lower() :
        continue
    
    print name,' --- ', pathString
    fileO.write(name+', '+pathString+"\n");

fileO.close()