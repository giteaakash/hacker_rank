import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input("please enter number").strip())
    print("...",n)
    if n % 2 != 0:
        print("Weird")
    if n % 2 == 0 and n in range(2,5):
        print("Not Weird")
    if n % 2 == 0 and n in range(6,21):
        print("Weird")
    if n % 2 == 0 and n > 20:
        print("Not Weird")