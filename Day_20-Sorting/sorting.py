#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
num_swaps=0
for j in range(n):
    for i in range(n-1):
        if(a[i]>a[i+1]):
            a[i],a[i+1]=a[i+1],a[i]
            num_swaps+=1
print("Array is sorted in {} swaps.".format(num_swaps))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[len(a)-1]))