#!/bin/python3

import math
import os
import random
import re
import sys

def myFirstFunction(n):
    if (n%2)!=0:
        print("Weird")
    elif(n%2)==0 and 2<=n and 5>=n:
        print("Not Weird")
    elif(n%2)==0 and 6<=n and 20>=n:
        print("Weird")
    elif(n%2)==0 and 20<n and 100>=n:
        print("Not Weird")

if __name__ == '__main__':
    n = int(input().strip())
    myFirstFunction(n)