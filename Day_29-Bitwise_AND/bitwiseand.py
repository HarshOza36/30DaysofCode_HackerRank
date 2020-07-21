#!/bin/python3

import math
import os
import random
import re
import sys

#Timeout error
# def getBitwise(n,k,max):
#     for i in range(1,n):
#         for b in range(i+1,n+1):
#             bi = i & b
#             if(bi>max and bi<k):
#                 max=bi
#     print(max)

if __name__ == '__main__':
    # t = int(input())
    # max = 0
    # n,k=[],[]
    # for t_itr in range(t):
    #     nk = input().split()
    #     n.append(int(nk[0]))
    #     k.append(int(nk[1]))
    #     getBitwise(n[t_itr],k[t_itr],max)
    
    T = int(input().strip())
    for _ in range(T):
        n , k = map(int , input().split())
        print(k-1 if ((k-1) | k) <= n else k-2)
