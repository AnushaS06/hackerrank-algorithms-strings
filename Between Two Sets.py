#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    i = 0
    total = 0
    l1 = max(a)
    l2 = max(b)
    l = max(l1,l2)
    while i <= l:
        i += 1
        isValidA = all(i % n == 0 for n in a)
        isValidB = all(n % i == 0 for n in b)
        if isValidA and isValidB:
            total += 1
    return (total)
    
    
    
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
