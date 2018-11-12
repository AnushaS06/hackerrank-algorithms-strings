#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    sorted(s)

    a_set = set()
    prev = ''

    count = 0
    for c in s:
        if c != prev:
            count = 1
            prev = c
        else:
            count +=1
        a_set.add(count * (ord(c) - 96))
    c=[]
    for i in queries:
        if i in a_set:
            c.append('Yes')
        else:
            c.append('No')
        #c += '\n'
    print(c)        
    return c
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
