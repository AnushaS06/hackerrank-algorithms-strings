#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the anagram function below.
def anagram(s):
    if(len(s)%2 != 0):
        return -1
    firstpart, secondpart = s[:round(len(s)/2)], s[round(len(s)/2):]
    firstpart=list(firstpart)
    secondpart=list(secondpart)
    for i in firstpart:
        if i in secondpart:
            #i=secondpart.index(i)
            secondpart.remove(i)
    return(len(secondpart))
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
