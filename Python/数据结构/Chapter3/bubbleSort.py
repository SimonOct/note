from swap import swap

def bubbleSort(lyst):
    n = len(lyst)
    while n > 1 :
        i = 1
        while i < n:
            if lyst[i] < lyst[i - 1]:
                swap(lyst, i, i - 1)
            i += 1
        n -= 1

lyst = [5, 3, 1, 2, 4]
print(f"before: {lyst}")
bubbleSort(lyst)
print(f"after: {lyst}")
# 该方法一共运行了86次才得出结果，虽然比选择排序好一点，但效率也不咋地
# 优化版，在这个例子来，可以发现执行到后面有几次的循环其实是没有必要的，因为循环一遍没有发生交换就已经意味着
# 排序完成，再循环多几遍也是在做无用功。因此可以设置布尔类型变量来让这种循环一遍没有发生交换情况下结束执行。
def bubbleSortOptimalize(lyst):
    n = len(lyst)
    while n > 1 :
        swapped = False
        i = 1
        while i < n:
            if lyst[i] < lyst[i - 1]:
                swap(lyst, i, i - 1)
                swapped = True
            i += 1
        if not swapped: return
        n -= 1
lyst = [5, 3, 1, 2, 4]
bubbleSortOptimalize(lyst)
print(f"after: {lyst}")
# 一共执行了88次，这个代码只能优化最好情况下的复杂度。因此复杂度都为O(n²)