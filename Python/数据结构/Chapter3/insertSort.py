
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

lyst = [5, 3, 1, 2, 4]
print(f"before: {lyst}")
insertSort(lyst)
print(f"after: {lyst}")
# 该方法一共运行了56次得出结果，好太多了。不过就是有点难理解过程，我在笔记上写一下过程