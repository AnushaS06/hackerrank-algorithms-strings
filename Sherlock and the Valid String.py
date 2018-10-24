#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the isValid function below.
def isValid(s):
    d = defaultdict(int) 
    for i in s:
        d[i] += 1
    c = d['a']
    count = 0
    for i in d:
        if(d[i] != c):
            count += 1
    if(count == len(s)-1 or count == 0 or count ==  1):
        return("YES")
    return("NO")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
