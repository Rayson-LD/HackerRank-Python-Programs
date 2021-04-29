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


#8
if __name__ == '__main__' :
    x, y, z, n = int(input()), int(input()), int(input()), int(input())
    print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if    a + b + c != n ])
    
#9
if __name__ == '__main__':
    n = int(raw_input())
    lis = list(map(int,raw_input().split()))
    print(sorted(list(set(lis)))[-2])
    
#10
if __name__ == '__main__' :
    grade = []
    for _ in range((int(input()))) :
        name = raw_input()
        score = float(input())
        grade.append([name,score])
    sort = sorted(list(set([x[1] for x in grade])))
    second = sort[1]
    final_list = []
    for student in grade :
        if second == student[1] :
            final_list.append(student[0])
    for student in sorted(final_list) :
        print(student)
        
#11
