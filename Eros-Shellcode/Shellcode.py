#!/usr/bin/env python
import os

file = raw_input("Input your ASM file path : ")
s_file = file.split('.')

os.system("nasm " + file + " -o " + s_file[0] + ".o")
os.system("ndisasm -u " + s_file[0] + ".o >> shelltemp")

fd = open("shelltemp", 'r')
os.system("touch shellcode1")
fl = open("shellcode1", 'w')
line = "".join(fd.readlines())

while line:
    tp = line.split(" ")
    fl.write(tp[2])
    line = "".join(fd.readlines())

fl.close()
fl = open("shellcode1", 'r')
code = fl.read(2)
os.system("touch shellcode")
fc = open("shellcode", 'w')
fc.write(r'shellcode[]="')

while code:
    fc.write(r"\x" + code)
    code = fl.read(2)

fc.write(r'";')
fl.close()
fc.close()
os.system("rm shellcode1")
fd.close()
os.system("rm shelltemp")