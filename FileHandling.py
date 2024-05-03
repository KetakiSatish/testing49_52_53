# File - is a container in computer storage to store the data ,
# any informational data (string)

# Python has several functions/methods for creating, reading, updating, and deleting files.

# The key function for working with files in Python is the "open()" function.

# The "open()" function takes two parameters; 'filename' and 'mode'.

# There are four different methods (modes) for opening a file:
# 1) "r" - Read - Default value. Opens a file for reading,
#          error if the file does not exist
# 2) "a" - Append - Opens a file for appending,
#          creates the file if it does not exist
# 3) "w" - Write - Opens a file for writing,
#          creates the file if it does not exist
# 4) "x" - Create - Creates the specified file,
#          returns an error if the file exists
# we have few advanced modes:
# a) 'r+' - to read and write data.
# b) 'w+' - to write and read data.
# c) 'a+' - to append and read the data.

f = open('demo.txt', 'w')
f.write("File handling is very easy... ")
# open the file#2 write content into it.


f = open('demo.txt', 'r')
print(f.read())
f.close()


f = open("demofile.txt")
#The code above is the same as:

f = open("demofile.txt", "rt")


f = open("Testing43.txt", "r")
print(f.read())

f = open("Testing43.txt", "w")
f.write("Testing 43 batch is good.")
f.close()


f = open("Testing43.txt", "w")
f.write("Testing 43 batch is good.")
f.close()

f = open("Testing43.txt", "r")
print(f.read())


You can return one line by using the readline() method:


f = open("Testing43.txt", "r")
#print(f.readline())
for i in f:
    print(i)


import os
os.remove("Testing43.txt")

f = open('demo.txt', 'w+')
f.write('we have to close the file which we opened.')

f = open('demo.txt', 'r+')
print(f.read())
f.close()

seek() & tell():

f = open("testing48", "w")
f.write("file handling is good.")
print(f.seek(3))
#print(f.tell()) #current position of pointer..
f.write("HANDLING")
f = open("testing48", "r")
print(f.read())
f.close() #seek() -->

context manager with file handling:

with open('testing48', 'r') as file: #context manager
    file_contai = file.read()
    print(file_contai) #close() no need..