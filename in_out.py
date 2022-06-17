print("Python is really a great language,", "isn't it?")

str = raw_input("Enter your input: ")
print("Received input is : ", str)

str = input("Enter your input: ")
print("Received input is : ", str)

# Open a file
fo = open("foo.txt", "wb")
print("Name of the file: ", fo.name)
print("Closed or not : ", fo.closed)
print("Opening mode : ", fo.mode)
print("Softspace flag : ", fo.softspac)

# Open a file
fo = open("foo.txt", "wb")
print("Name of the file: ", fo.name)

# Close opend file
fo.close()

# Open a file
fo = open("foo.txt", "wb")
fo.write( "Python is a great language.\nYeah its great!!\n")

# Close opend file
fo.close()

# Open a file
fo = open("foo.txt", "r+")
str = fo.read(10);
print("Read String is : ", str)
# Close opend file
fo.close()

# Open a file
fo = open("foo.txt", "r+")
str = fo.read(10)
print "Read String is : ", str

# Check current position
position = fo.tell()
print "Current file position : ", position

# Reposition pointer at the beginning once again
position = fo.seek(0, 0);
str = fo.read(10)
print("Again read String is : ", str)
# Close opend file
fo.close()

import os

# Rename a file from test1.txt to test2.txt
os.rename( "test1.txt", "test2.txt" )

import os

# Delete file test2.txt
os.remove("text2.txt")

import os

# Create a directory "test"
os.mkdir("test")


import os

# Changing a directory to "/home/newdir"
os.chdir("/home/newdir")

# This would give location of the current directory
os.getcwd()

# This would  remove "/tmp/test"  directory.
os.rmdir( "/tmp/test"  )
