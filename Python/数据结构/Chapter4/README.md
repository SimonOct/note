

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

二维数组是一种数据结构，将数据组织在行和列中。每个元素都可以使用两个下标来访问或替换，下标指定了元素的行和列，可以随机访问。

A two dimensional array is a data structure that organizes data in rows and columns. Each item can be accessed or replaced with random access using two subscripts, which specify the row and column of the item.

### 请描述一个可能会用到二维数组的应用程序

一个二维数组可能被用来表示游戏程序中的棋盘。

A two-dimensional array might be used to represent a checkerboard in a game-playing program.

# 4.5 单项链接结构上的操作

## 练习题

### 假设已经找到了从单向链接结构里删除元素的位置，请说明从这个时候开始完成删除操作的运行时复杂度

在元素被定位后，从单链结构中删除一个元素的运行时间复杂度为O(1)。

The run-time complexity for removing an item from a singly linked structure after that item has been located is O(1).

### 可以对单向链接结构里按顺序排序的元素执行二分搜索吗？如果不可以，为什么

在一个单链结构上对一个元素进行二分搜索是不现实的。定位中点的运行时间成本将是线性的，所以这种搜索的运行时间将比顺序搜索的运行时间更差。

It is not practical to perform a binary search for an item on a singly linked structure. The runtime cost of locating the midpoint would be linear, so the running time of such a search would be worse than that of a sequential search.

### 请说明为什么Python列表会使用数组而不是链接结构来保存它的元素

Python list 使用数组而不是链接结构来保存它的元素，因为访问和替换操作的运行时间是 O(1)，而且当数组的一半以上的位置被占用时，内存的使用效果更好。

A Python list uses an array rather than a linked structure to hold its items because the running times of the access and replacement operations are O(1), and the memory usage is better when more than half of the array’s positions are occupied.

# 4.6 链接上的变化

## 练习题

### 包含虚拟头节点的环状链接结构给程序员带来了什么好处

一个带有虚拟头节点的循环链接结构使程序员能够避免在代码中插入或删除结构头部和尾部的元素的特殊情况。

A circular linked structure with a dummy header node enables the programmer to avoid special cases in the code for inserting or removing items at the head and tail of the structure.

### 和单向链接结构相比，请描述双向链接结构的一个好处和一个额外开销

双链结构的一个好处是，移动到前一个项目的操作在恒定的时间内运行。一个代价是，每个节点的第二个链接需要一个额外的存储单元。

One benefit of a doubly linked structure is that the operation to move to a previous item runs in constant time. One cost is that an extra memory cell is required for the second link in each node.

# 总结

- 数据结构是一个表示多项集里所包含数据的对象
- 数组是一种在常数时间内支持对位置逐项随机访问的数据结构。在创建数组时，会为它分配若干个用来存放数据的内存空间，并且数组的长度会保持不变。插入和删除操作需要移动数据元素，并且可能需要创建一个新的、更大或更小的数组
- 二维数组里的每个数据值都位于矩形网格的行和列上
- 链接结构是由0个或多个节点组成的数据结构。每个节点都包含一个数据结构和一个或多个指向其它节点的链接
- 单向链接结构的节点包含数据元素和到下一个节点的链接。双向链接结构里的节点还包含到前一个节点的链接
- 在链接结构里进行插入或删除操作不需要移动数据元素每次最多只会创建一个节点。但是，在链接结构里执行插入、删除和访问操作需要的时间复杂度都是线性的
- 在链接结构里使用头节点可以简化某些操作，如添加或删除元素
