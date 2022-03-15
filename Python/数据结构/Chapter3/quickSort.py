import random


def swap(lyst, i, j):
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp


def quicksort(lyst):
    quicksortHelper(lyst, 0, len(lyst) - 1)


def quicksortHelper(lyst, left, right):
    if left < right:
        pivot_location = partition(lyst, left, right)
        quicksortHelper(lyst, left, pivot_location - 1)
        quicksortHelper(lyst, pivot_location + 1, right)


def partition(lyst, left, right):
    middle = (left + right) // 2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot

    boundary = left

    for index in range(left, right):
        if lyst[index] < pivot:
            swap(lyst, index, boundary)
            boundary += 1

    swap(lyst, right, boundary)
    return boundary

def main(size=20, sort=quicksort):
    lyst = []
    for count in range(size):
        lyst.append(random.randint(1, size + 1))
    print(lyst)
    sort(lyst)
    print(lyst)


if __name__ == "__main__":
    main()

# 这个算法比前面三个快得太多，数据越大，使用时间的差距就越大