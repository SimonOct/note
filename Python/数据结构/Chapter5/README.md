# 5.2 构造函数和类的实现

## 练习题

### 包里的元素是有序的，还是无序的

包里的元素是无序的

The items in a bag are unordered.

### 哪些操作会出现在所有多项集的接口里

isEmpty, len, str, iter, add, ==, +操作出现在任何集合的接口中。

The isEmpty, len, str, iter, add, ==, and + operations appear in the interface of any collection..

### 哪个方法负责创建多项集对象

`__init__`方法负责创建一个集合对象。

The `__init__` method is responsible for creating a collection object.

### 请说出接口与实现分离的3个原因

接口与实现是分开的，因为
		a. 实现的代码可以被修改而不需要重写使用它的代码。
		b. 可以选择一个完全不同的实现，只要它符合接口的要求。
		c. 一个接口的用户不必关心其实现的任何细节。

Interfaces are separated from implementations because

​     a. The code for an implementation can be modified without rewriting the code that uses it.

​     b. A completely different implementation can be chosen, as long as it conforms to the interface.

​     c. The user of an interface does not have to be concerned with any details of its implementation.

# 5.3  开发基于数组的实现

## 练习题

### 解释多项集类的`__init__`方法的作用

一个集合类的`__init__`方法负责创建一个容器对象的实例，将逻辑大小设置为0，并将数据项从一个源集合复制到新的集合。

The `__init__` method of a collection class is responsible for creating an instance of a container object, setting the logical size to 0, and copying data items from a source collection to the new collection.

### 为什么调用方法比直接在类里引用实例变量更好

在一个类中，调用方法比引用实例变量要好，因为方法是接口的一部分，它永远不会改变，而变量不是，所以它们可能会改变。因此，使用方法调用而不是变量引用使代码更稳定，更容易分享。

It’s better to call methods than to refer to instance variables in a class, because methods are part of an interface, which never changes, whereas variable are not, and so they may change. Thus, the use of method calls rather than variable references makes code more stable and easier to share.

### 对于ArrayBag的`__init__`方法，展示如何通过调用clear方法来简化代码

```python
def __init__(self, sourceCollection = None):

  self.clear()

if sourceCollection:

  for item in sourceCollection: self.add(item)
```

### 解释为什么`__iter__`方法可能会是多项集类里最有用的方法

方法`__str__`、`__add__`和`__eq__`都是在self上通过使用for循环来完成的

### 解释为什么在ArrayBag类中不用包含`__contains__`方法

当 Python 在一个集合类中没有看到 `__contains__` 方法时，它会自动创建一个，使用 `__iter__` 方法来对集合进行线性搜索。

When Python does not see a `__contains__` method in a collection class, it automatically creates one, using the `__iter__` method to perform a linear search on the collection.

# 5.4 开发基于链接的实现

## 练习题

### 假设a是一个数组包，b是一个链接包，它们都不包含任何元素。请描述在这种情况下它们在内存使用上的差异

数组实例化后就会占用数组包默认容量大小的内存，无论里面是否含有元素。但是链表不含元素时，仅仅只实例化了变量，内存使用量相对与数组来说就小得多

### 为什么链接包任然需要一个单独的实例来记录它的逻辑尺寸

这样可以避免每次使用`len()`计算长度时都需要遍历整条链表

### 为什么从链接包里删除元素之后，程序员不用担心出现内存浪费的情况

当执行删除操作后，该元素会断开与链表的链接，并被GC回收



# 总结

- 接口是用户的软件资源可以使用的一组操作
- 接口里的元素是函数和方法的定义以及它们的文档
- 前置条件是指在函数或方法可以完全正确完成任务之前必须要满足的条件
- 后置条件是指在函数或方法正确完成任务之后必须为真的条件
- 设计良好的软件系统会把节后和它的实现分开
- 实现是指满足接口的函数、方法或类
- 多项集类型可以通过接口进行指定
- 多项集类型可以有几个不同的实现类
- 多态是指在两个或多个实现里使用相同的运算符、函数名称或方法名称。多态函数的示例是str和len；多态运算符的示例是+和==；多态方法的示例包括add和isEmpty
- 包多项集是无序的，并且支持添加、删除和访问其元素等操作
- 类图是一种描述类与类之间关系的可视化表示方法
- 组合表示两个类之间整体与局部的关系
- 聚合表示两个类之间一对多的关系
- UML是一种描述软件资源之间关系的可视化 表示方法

