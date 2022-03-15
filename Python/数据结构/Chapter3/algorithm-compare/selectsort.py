#!/usr/bin/python3
import random
import time

def swap(lyst, i, j):

    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp
    

def selectSort(lyst):
    i = 0
    while i < len(lyst):
        minIndex = i
        j = i + 1
        while j < len(lyst):
            if lyst[j] < lyst[minIndex]:
                minIndex = j
            j += 1

        if minIndex != i:
            swap(lyst, minIndex, i)
        i += 1

lyst = []
size = 10000
for count in range(size):
    lyst.append(random.randint(1, size + 1))
start = time.time()
selectSort(lyst)
end = time.time() - start
print(f"Time used: {end}")
