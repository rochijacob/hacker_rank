import math
import os
import random
import re
import sys
import functools

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    sum = functools.reduce(lambda a, b: a+b, arr)
    max_e = functools.reduce(lambda a, b: a if a > b else b, arr) #Max element
    min_e = functools.reduce(lambda a, b: a if a < b else b, arr)
    
    max = sum - min_e
    min = sum - max_e
    
    print(min, max)
        
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
