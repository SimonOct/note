#!/usr/bin/python3
import random
import time

def insertSort(lyst):
    i = 1
    while i < len(lyst):
        itemToInsert = lyst[i]
        j = i - 1
        while j >= 0:
            if itemToInsert < lyst[j]:
                lyst[j + 1] = lyst[j]
                j -= 1
            else:
                break
        lyst[j + 1] = itemToInsert
        i += 1

lyst = []
size = 10000
for count in range(size):
    lyst.append(random.randint(1, size + 1))
start = time.time()
insertSort(lyst)
end = time.time() - start
print(f"Time used: {end}")
