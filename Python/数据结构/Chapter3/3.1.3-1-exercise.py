# 1.编写一个测试程序，这个程序统计并显示出下面这个循环的迭代次数
# while problemSize > 0:
#     problemSize = problemSize // 2
# 这是我的答案
problemSize = [1000, 2000, 4000, 10000, 100000]
print("%12s%15s" % ("problemSize", "Interations"))
for count in range(5):
    number = 0
    size = problemSize[count]
    while size > 0:
        number += 1
        size = size // 2
    print("%12d%15d" % (problemSize[count], number))

# 2.在问题规模分别为1000、2000、4000、10000和100000时，运行在练习1里所创建的程序。当问题规模翻倍或是乘以10时，迭代次数会如何变化？
# 答：当翻倍的时候，迭代次数增加1.当乘以10时，迭代次数增加3.