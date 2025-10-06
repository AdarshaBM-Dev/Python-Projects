#w - write
# a -append
#x - create and write
#r - read
#t -text
#b - binary
'''f = open("Adarsha.jpg", "rb")
print(f.read())

f = open("sneha.txt", "rt")
print(f.read())

f = open("sneha.txt", "w")
f.write("hi Sneha")

f = open("sneha.txt", "a")
f.write("hi Sneha")

f = open("sneha5.txt", "x")
f.write("hi Sneha")
f.close()

#delete file
import os
os.remove("sneha5.txt")

# floder create
import os
os.mkdir("sneha")'''
#remove file
import os
os.rmdir("sneha")
