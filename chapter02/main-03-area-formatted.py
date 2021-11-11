from numpy import *
from sys import version

if int(version[0]) > 2:
    raw_input = input

name = raw_input('Key in your name: ')
print('Hi ', name)
radius = eval(raw_input('Enter a radius: '))  # for numerical values
print('your entered radius = %8.5f' % radius)  # formatted output
print('Enter new name and r in file Name.dat')  # raw_input string

# noinspection SpellCheckingInspection
inpfile = open('Name.dat', 'r')  # Read from file Name.dat

for line in inpfile:
    line = line.split()  # Splits components of line
    name = line[0]  # First entry in the list
    print(' Hi %10s' % (name))  # print Hi + first entry
    r = float(line[1])  # convert string to float
    print(' r = %13.5f' % (r))  # convert to float & print
inpfile.close()

A = math.pi * r ** 2
print('Done, look in A.dat\n')
outfile = open('A.dat', 'w')
outfile.write('r = %13.5f\n' % r)
outfile.write('A = %13.5f\n' % A)
outfile.close()
print('r = %13.5f' % (r), ', A = %13.5f' % A)
print('\n Now example of integer input ')
age = int(eval(raw_input('Now key in your age as an integer: ')))
print("age: %4d years old, you don't look it!\n" % age)
print('Enter and return a character to finish')
s = raw_input()
