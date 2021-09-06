#!/usr/bin/python
#Author : Amitava Chakraborty

#File I/O with Python

# Open a file
fo = open("datafile-01.dat", "r")

#Other modes
#rb, r+, rb+
#w, wb, w+, wb+
#a, ab, a+, ab+

print "Name of the file: ", fo.name
print "Closed or not : ", fo.closed
print "Opening mode : ", fo.mode
print "Softspace flag : ", fo.softspace

#Read 10 bytes from the file
print 'First 10 bytes : ',fo.read(10)

#Current file position
print 'Current position : ',fo.tell()

#Seek a position
#fo.seek(offset [,from])
#Go 10 bytes from current position(1)
fo.seek(1,10)
#Go to end(2) of file
fo.seek(2)
#Go to the beginning(0) of file
fo.seek(0)

#Read five lines from the file
for index in range(5):
   line = fo.next()
   print "Line No %d - %s" % (index, line)

#We want to reread - hence we have to take the cursor in the beginning
fo.seek(0)
#Read All lines
lines = fo.readlines()
print "Read Line: %s" % (lines)

#Close a file
fo.close()