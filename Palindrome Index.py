#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
def isPalindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True
 

def palindromeIndex(s):
    if(s == s[::-1]):
        return(-1)
    for i in range((len(s)+1)//2):
        if s[i] != s[len(s)-i-1]:
            if isPalindrome(s[:i]+s[i+1:]):
                return i
            else:
                return len(s)-i-1
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
