from swap import swap

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

lyst = [5, 3, 1, 2, 4]
print(f"before: {lyst}")
selectSort(lyst)
print(f"after: {lyst}")
# 该方法一共运行了91次才得出结果，效率不咋地，复杂度为O(n²)