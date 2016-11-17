from math import *
PI = 3.14
a = input("Enter the length of your 1st side:")
b = input("Enter the length of your 2nd side:")
c = input("Enter the measurment of your known angle:")
r = float(c)*PI/180
a = (1/2)*(float(a)*float(b))*sin(r)                                 
print("The area of your triangle is", a)