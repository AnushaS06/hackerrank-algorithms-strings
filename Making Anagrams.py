#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    d = defaultdict(int) 
    for i in s1:
        d[i] += 1
        #print(d[i])
    for i in s2:
        d[i] -= 1
    count = 0
    for i in d:
        count += abs(d[i]) 
        #print(d[i])
    return(count)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
