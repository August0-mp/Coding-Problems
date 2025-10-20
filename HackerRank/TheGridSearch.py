#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#

def gridSearch(G, P):
    nb_rows = len(P)
    nb_columns = len(P[0])
    m = len(G)
    n = len(G[0])
    
    def compare(i, j):
        for ii in range(nb_rows):
            for jj in range(nb_columns):
                if G[i+ii][j+jj] != P[ii][jj]:
                    return False
        return True
            
        
    for i in range(m-nb_rows+1):
        for j in range(n-nb_columns+1):
            if G[i][j] == P[0][0]:
                if compare(i,j):
                    return "YES"
                    
    return "NO"
                    
                
                    
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
