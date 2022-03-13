
def binarySearch(target, sortedLyst):
    left = 0
    right = len(sortedLyst) - 1
    while left <= right:
        midpoint = (left + right) // 2
        print(f"before midponit: {midpoint}, left: {left}, right: {right}")
        if target == sortedLyst[midpoint]:
            return midpoint
        elif target < sortedLyst[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
        print(f"after midponit: {midpoint}, left: {left}, right: {right}\n")
    return -1

lyst = [20, 44, 48, 55, 62, 66, 74, 88, 93, 99]
binarySearch(44, lyst)