#!/bin/python3

import sys


def fibonnacci(n):
    n0 = 1
    n1 = 2
    ans = 0
    while n1<n:
        if n1%2==0:
            ans+=n1
        t = n0
        n0 = n1
        n1 += t
        
    return ans

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(fibonnacci(n))

# https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem