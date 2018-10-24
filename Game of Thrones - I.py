#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    s1 = list(set(s))
    count = 0
    for i in range(len(s1)):
        c=s.count(s1[i])
        if(c % 2 != 0):
            count += 1
            if(count > 1):
                return("NO")
    return("YES")
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
