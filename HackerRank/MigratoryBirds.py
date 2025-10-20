#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    freq = {0:0}
    id_ = 0
    for b in arr:
        if b in freq.keys():
            freq[b]+=1
            if freq[b]>freq[id_]:
                id_=b
            elif freq[b]==freq[id_] and b<id_:
                id_=b
        else:
            freq[b]=1
    return id_
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
