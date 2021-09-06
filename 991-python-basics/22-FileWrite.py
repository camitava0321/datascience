import sys

#Print to stdout
print 'Enter a file name where the program will write something : ',

#variables
file_finish="$"
file_text=" "

#Accept a raw input
file_name = raw_input()

try:
# open file stream
    file = open(file_name, "w")
except IOError:
  print ("There was an error writing to", file_name)
  sys.exit()
print ("Enter '", file_finish,)
print "' When finished"
while file_text != file_finish:
  file_text = raw_input("Enter text: ")
  if file_text == file_finish:
    break
  file.write(file_text)
  file.write("\n")
file.close()

try:
  file = open(file_name, "r")
except IOError:
  print ("There was an error reading file")
  sys.exit()

print "Following lines have been written in the file ",file_name
file_text = file.read()
file.close()
print (file_text)