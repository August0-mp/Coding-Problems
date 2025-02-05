#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    n3 = (n-1)//3
    n5 = (n-1)//5
    n15 = (n-1)//15  

    s3 = (3+n3*3)*(n3)//2

    s5 = (5+n5*5)*(n5)//2

    s15 = (15+n15*15)*(n15)//2

    print(s3+s5-s15)
        
# https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem