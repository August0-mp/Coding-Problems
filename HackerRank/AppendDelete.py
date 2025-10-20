#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    i = 0
    ls = len(s)
    lt = len(t)
    if k>=ls+lt:
        return "Yes"
    
    while i<ls and i<lt and s[i] == t[i]:
        i+=1
    n_op = k - (ls - i + lt -i)
    
    if n_op >= 0 and n_op%2==0:
        return "Yes"
        
    return "No"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
