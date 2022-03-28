from arrays import Array

class ArrayBag(object):
    """An array-based bag implementation."""
    # 一个基于数组的包的实现。

    # Class variable
    # Class变量
    DEFAULT_CAPACITY = 10
    PHYSICAL_SIZE = 10

    # Constructor
    # 构建器
    def __init__(self, sourceColletion=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        # 设置self的初始状态，包括sourceCollection的内容，如果它存在的话。
        self.items = Array(ArrayBag.DEFAULT_CAPACITY)
        self.size = 0
        if sourceColletion:
            for item in sourceColletion:
                self.add(item)

    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        # 如果len(self) == 0的话返回True，否则返回False。
        return len(self) == 0

    def __len__(self):
        """Returns the number of items in self."""
        return self.size

    def clear(self):
        """Makes self become empty."""
        self.size = 0
        self.items = Array(self.DEFAULT_CAPACITY)

    def add(self, item):
        """Adds item to self."""
        # 当数组长度大于等于PHYSICAL_SIZE时，对其进行扩容，每次比原本容量增大两倍
        if len(self) >= self.PHYSICAL_SIZE:
            self.PHYSICAL_SIZE *= 2
            self.adjusting_capacity(self.PHYSICAL_SIZE)

        self.items[len(self)] = item
        self.size += 1

    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < len(self):
            # yield这个语句能让for循环时执行while并返回结果，而不是让while执行完成后再用for循环将结果
            # 一一打印出来，好处就是能降低内存占用，因为这样就不需要完整地存while执行结果了嘛
            # 它与return的一个区别就是yield不会打断循环。
            yield self.items[cursor]
            cursor += 1

    def __str__(self):
        """Returns the string representation of self."""
        # 返回self的字符串表示法。
        # ", ".join() 的意思是把 逗号空格 作为连接词
        return "{" + ", ".join(map(str, self)) + "}"

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        result = ArrayBag(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other) -> bool:
        """Returns True if self equals other,
        or False otherwise."""
        if self is other:
            return True
        # 如果是通过这个class实例化出来的数组，类型应该是<class 'arraybag.ArrayBag'>
        if type(self) != type(other) or \
                len(self) != len(other):
            return False
        for item in self:
            if self.count(item) != other.count(item):
                return False
        # 判断两个数组的方法是通过计数的方式，我猜可能这样会更快的得出结果，因为只要有一个数的数量不同就False了
        return True

    def count(self, item: int) -> int:
        """Returns the number of instances of item in self."""
        # 统计某个数字在这个数组出现多少次，并返回值，注意参数类型，不同类型只会统计某个类型的总数
        total = 0
        for nextItem in self:
            if nextItem == item:
                total += 1
        return total

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Post-condition: item is removed from self."""
        # Check precondition and raise if necessary
        if not item in self:
            raise KeyError(str(item) + " not in bag")
        # Search for the index of the target item
        targetIndex = 0
        for targetItem in self:
            if targetItem == item:
                break
            targetIndex += 1
        # Shift items to the left of target up by one position
        for i in range(targetIndex, len(self) - 1):
            self.items[i] = self.items[i + 1]
        # Decrement logical size
        self.size -= 1
        # Check array memory here and decrease it if necessary
        # Exercise
        # 当数组实际使用的容量比默认容量大，并且只使用了PHYSICAL_SIZE四分之一的时，对其进行缩容，
        # 容量为实际使用的两倍
        if self.PHYSICAL_SIZE // 4 >= len(self) > self.DEFAULT_CAPACITY:
            self.PHYSICAL_SIZE = len(self) * 2
            self.adjusting_capacity(self.PHYSICAL_SIZE)
        elif len(self) < self.DEFAULT_CAPACITY:
            self.PHYSICAL_SIZE = self.DEFAULT_CAPACITY
            self.adjusting_capacity(self.PHYSICAL_SIZE)

    # 调整数组容量
    def adjusting_capacity(self, capacity):
        tmp = Array(capacity)
        for i in range(0, len(self)):
            tmp[i] = self.items[i]
        self.items = tmp


if __name__ == "__main__":
    # 测试扩容缩容
    a, b = ArrayBag(), ArrayBag()
    for i in range(1, 31):
        a.add(i)
        b.add(i)
    c = a + b
    print(f"PHYSICAL_SIZE: {c.PHYSICAL_SIZE}\nlength is: {len(c)}")
    for i in range(1, 31):
        c.remove(i)
    print(f"\nremoved 30 words")
    print(f"PHYSICAL_SIZE: {c.PHYSICAL_SIZE}\nlength is: {len(c)}")
    for i in range(1, 11):
        c.remove(i)
    print(f"\nremoved 10 words")
    print(f"PHYSICAL_SIZE: {c.PHYSICAL_SIZE}\nlength is: {len(c)}")
    for i in range(11, 29):
        c.remove(i)
    print(f"\nremoved 18 words")
    print(f"PHYSICAL_SIZE: {c.PHYSICAL_SIZE}\nlength is: {len(c)}")