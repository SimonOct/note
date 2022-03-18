

# 4.1 数组数据结构

## 示例

```python
>>> from arrays import Array
>>> a = Array(5)
>>> len(a)
5
>>> print(a)
[None, None, None, None, None]
>>> for i in range(len(a)):
...     a[i] = i + 1
...
>>> a[0]
1
>>> for item in a:
...     print(item)
...
1
2
3
4
5
```

## 练习题

### 请说明随机访问的工作原理，以及这个操作这么快的原因

随机访问使用数据的基址和数组中某个位置的索引来定位内存中与该位置对应的单元。

它通过将索引值乘以数据值的大小的结构添加到机制中实现。

因为这是一个恒定的时间操作，所以无论访问哪个位置，随机访问都是一个恒定时间操作。

Random access uses the base address of an array and the index of a position in the array to locate the cell in memory corresponding to the position. It does this by adding to the base address the result of multiplying the index value by the size of the data value. Because this is a constant time operation, random access is a constant time operation, no matter which position is accessed.

### 数据和Python列表之间有什么区别

本章里关于数组的很多内容也同样是用于python列表，但是数据的限制要更多。

程序员只能在指定位置访问和替换数组中的元素、检查数组的长度、获取它的字符串表达式。

程序员不能基于位置添加或删除元素，也不能对数组的长度进行修改。通常来说，数组的长度也就是它的容量，在创建之后是固定的。

An array allows the user to access or replace items with a subscript operation at given positions in a structure of fixed size, whereas a list allows the user to insert or remove items, automatically adjusting the size of the structure if necessary. A list tracks the number of items currently in it and available to the user.

### 请说明数组的物理尺寸和逻辑尺寸之间的区别

数组的物理尺寸是指可用于存储项目的单元格或位置的数量，在创建数组时是固定的。

数组的逻辑尺寸是数组中当前可供用户使用的元素数量，起范围为0~（物理尺寸 - 1）。

The physical size of an array is the number of cells or positions available for storing items, which is fixed when the array is created. The logical size of an array is the number of items currently in it and available to the user, which ranges from 0 to the physical size minus 1.

# 4.2 数组的操作

## 练习题

### 请说明为什么插入或删除给定元素时必须要移动数组里的某些元素

如果一个元素在数组的逻辑末端被移除或插入，其它元素不需要被移位。

如果一个元素在其它地方被移除，其右边的元素必须向左移动一个位置，以填补被移除的元素所腾出的空间。

如果一个元素被插入到其它地方，从目标索引到最后一个逻辑位置的元素必须向右移动一个位置，以便为新的项目腾出空位。

If an item is removed or inserted at the logical end of an array, no other items have to be shifted. If an item is removed anywhere else, the items to its right must be shifted to the left by one position to close the hole vacated by the removed item. If an item is inserted anywhere else, the items from the target index down to the last logical position must be shifted to the right by one position to open a hole for the new item.

### 在插入过程中，移动数组元素时，要先移动哪个元素？先移动插入位置的元素，还是最后一个元素

在一个数组中插入一个元素时，最后一个逻辑位置的元素首先被移到右边。

这就为它的前身打开了一个洞，这样它就可以向右移动，以此类推，直到最终在目标位置为插入的项目打开一个洞。

这样做的原因是为了使一个被移动的元素不至于打击到它旁边的元素。

During an insertion of an item into an array, the item at the last logical position is moved to the right first. This opens a hole for its predecessor so it can be moved to the right, and so on, until a hole is eventually opened at the target position for the inserted item. The reason this is done is so that a moved item does not clobber the item next to it.

### 如果插入位置是数组的逻辑末尾，请说明这个插入操作的运行时复杂度

当空间可用时，其复杂度为O(1)。

如果空间不可用，复杂性为O(n)，因为要调整数组的大小。

如果每次调整阵列大小都要加倍，那么在阵列的逻辑末端插入的复杂性平均为O(1)。

The complexity is O(1) when space is available. If space is unavailable, the complexity is O(n), because of resizing the array. If the array size is doubled every time resizing occurs, the complexity of an insertion at the logical end of the array is O(1) on the average.

### 假设数组当前包含14个元素，它的负载因子为0.70，那么它的物理容量是多少

该数组的容量为14/0.70，即20。

The array’s capacity is 14/0.70, or 20. 

# 4.3 二维数组（网格）

## 练习题

### 什么是二维数组（网格）



A two dimensional array is a data structure that organizes data in rows and columns. Each item can be accessed or replaced with random access using two subscripts, which specify the row and column of the item.
