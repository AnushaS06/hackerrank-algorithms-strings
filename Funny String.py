#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    r=s[::-1]
    t=[]
    u=[]
    for i in range(len(s)):
        t.append(ord(s[i]))
        u.append(ord(r[i]))
    sub1=[]
    sub2=[]
    for i in range(len(s)-1):
        sub1.append(abs(t[i] - t[i+1]))
        sub2.append(abs(u[i] - u[i+1]))
    print(sub1,sub2)
    if(sub1==sub2):
        return("Funny")
    return("Not Funny")
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
