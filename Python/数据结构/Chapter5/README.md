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
