# 3.4.3 插入排序(insertSort)

这个排序方法就像给手上的扑克牌排序一样

## 第一次排序

![未命名文件1](README.assets/%E6%9C%AA%E5%91%BD%E5%90%8D%E6%96%87%E4%BB%B61-16472771514202.png)

- 将位置1的值存到变量itemToInsert下
- 然后比较itemToInsert与列表[0]的大小
- 因为5比3大，将列表[1]更改为5
- 最后将列表[0]修改为itemToInsert的值

![未命名文件1](README.assets/%E6%9C%AA%E5%91%BD%E5%90%8D%E6%96%87%E4%BB%B61.png)

## 第二次排序

![未命名文件(1)](README.assets/%E6%9C%AA%E5%91%BD%E5%90%8D%E6%96%87%E4%BB%B6(1)-16472769445871.png)

- 将位置2的值存到变量itemToInsert下
- 然后比较itemToInsert与列表[1]的大小
- 列表[1]的大，于是将列表[2]的值修改成列表[1]的值
- 比较itemToInsert与列表[0]的大小
- 列表[0]的大，于是将列表[1]的值修改成列表[0]的值
- 最后将列表[0]修改为itemToInsert的值

![未命名文件1(1)](README.assets/%E6%9C%AA%E5%91%BD%E5%90%8D%E6%96%87%E4%BB%B61(1).png)

## 第n次排序

接下来的操作就不一一介绍了，可以比作一手牌排序。

假设一手牌没有重复，从小到大排，一次排一张，从第二张开始排。

# 总结

- 根据所需要的时间和内存资源，我们可以对解决同一个问题的不同算法进行排名。与需要更多资源的算法相比，我们通常认为耗费更少运行时和占用更少内存的算法更好。但是，这两种资源也通常需要进行权衡取舍：有时以更多内存为代价来改善运行时；有时以较慢的运行时作为代价来提高内存的使用率。
- 可以根据计算机的时钟按照过往经验测算算法的运行时。但是，这个时间会随着硬件和所用编程语言的不同而变化。
- 统计指令的数量提供了另一种对算法所需工作量进行经验性度量的方式。指令的计数可以显示出算法工作量的增长率的变化，而且这个数据和硬件以及软件平合都没有关系。
- 算法工作量的增长率可以用基于问题规模的函数来表示。复杂度分析查看算法里的代码以得到这些数学表达式，从而让程序员预测在任何计算机上执行这个算法的效果。
- 大O表示法是用来表示算法运行时行为的常用方法。它用 O(f(n))的形式来表示解决这个问题所需要的工作量，其中n是算法问题的规模f(n)是数学函数。
- 运行时行为的常见表达式有O(log₂n)（对数）、O(n)（线性）、O(n²)（平方）以及O(kⁿ)（指数）。
- 算法在最好情况、最坏情况以及平均情况下的性能可以是不同的。比如，冒泡排序和插入排序在最好情况下都是线性复杂度，但是它们在平均情况和最坏情况下是平方阶复杂度。
- 通常来说，要提高算法的性能最好是尝试降低它的运行时复杂度的阶数，而不是对代码进行微调。
- 二分搜索会比顺序搜索要快得多。但是，在用二分搜索进行搜索时，数据必须是有序的。
