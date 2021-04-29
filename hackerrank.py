import math
import os
import random
import re
import sys
from __future__ import division
from __future__ import print_function

#1
if __name__ == '__main__':
    print("Hello World !")

#2
if __name__ == '__main__':
    n = int(raw_input().strip())
if n%2 != 0 :
    print("Weird")
if n>=2 and n<=5 :
    if n%2 == 0 :
        print("Not Weird")
        
if n>=6 and n<=20 :
    if n%2 == 0 :
        print("Weird")
if n>20 :
    if n%2 == 0 :
        print("Not Weird")

        
#3
if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
s = a +b
m = a - b
p = a*b 
print(s)
print(m)
print(p)

#4
if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())

s = a//b
d =a/b
print(s)
print(d)

#5
if __name__ == '__main__':
    n = int(raw_input())
for i in range(0,n) :
    a = i*i
    print(a)

#6
def is_leap(year):
    leap = False
    
    if year%4 == 0 and year%100 != 0 :
        leap = True
        return leap
    elif year%400 == 0 :
        leap = True
        return leap
    elif year%100 == 0 :
        leap = False
        return leap    
    else :
        return False

#7
if __name__ == '__main__':
    n = int(raw_input())

for i in range(1,n+1) :
    print(i,end="")




