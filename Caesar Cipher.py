#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    l = []
    for i in range(len(s)):
        if (s[i].isalpha()):
            l.append(ord(s[i])+(k%26))
            if(s[i].islower()):
                if(l[i] > 122):
                    l[i] = 97 +abs(123-l[i])
            else:
                if(l[i] > 90):
                    l[i] = 65 +abs(91-l[i])
            l[i] = chr(l[i])
        else:
            l.append(s[i])
        
    str1 = ''.join(l)
    return(str1)
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
