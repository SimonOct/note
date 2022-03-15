#!/usr/bin/python3
import random
import time

def swap(lyst, i, j):

    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp
    

def bubbleSort(lyst):
    n = len(lyst)
    while n > 1 :
        i = 1
        while i < n:
            if lyst[i] < lyst[i - 1]:
                swap(lyst, i, i - 1)
            i += 1
        n -= 1

lyst = []
size = 10000
for count in range(size):
    lyst.append(random.randint(1, size + 1))
start = time.time()
bubbleSort(lyst)
end = time.time() - start
print(f"Time used: {end}")
