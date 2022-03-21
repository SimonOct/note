class Node(object):

    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous


class TwoWayNode(object):

    def __init__(self, item=None):
        if item is None:
            self.__head = item
            self.__tail = item
        else:
            node = Node(item)
            self.__head = node
            self.__tail = node

    def isEmpty(self) -> bool:
        return self.__head is None

    def length(self) -> int:
        count = 0
        current = self.__head
        while current is not None:
            count += 1
            current = current.next

        return int(count)

    def traversal(self, beginning="head"):

        if beginning == "tail":
            current = self.__tail
            while current is not None:
                print(current.data, end=" ")
                current = current.previous
        else:
            current = self.__head
            while current is not None:
                print(current.data, end=" ")
                current = current.next
        print("")

    def add(self, item):
        new_node = Node(item)
        if self.isEmpty():
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.next = self.__head
            self.__head.previous = new_node
            self.__head = new_node

    def append(self, item):
        new_node = Node(item)
        if self.isEmpty():
            self.__head = new_node
            self.__tail = new_node
        else:
            current = self.__head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.previous = current
            self.__tail = new_node

    def search(self, item):
        current = self.__head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

    def insert(self, position: int, item):
        if position <= 0:
            self.add(item)
        elif position >= self.length():
            self.append(item)
        else:
            new_node = Node(item)
            current = self.__head
            count = 0
            while count < (position - 1):
                count += 1
                current = current.next

            new_node.previous = current
            new_node.next = current.next
            current.next.previous = new_node
            current.next = new_node

    def remove(self, item):
        # 是不是头节点
        if self.__head.data == item:
            self.__head = self.__head.next
            # 判断删除后存不存在一个节点
            if self.__head.next:
                self.__head.previous = None
            return
        current = self.__head
        while current is not None:
            if current.data == item:
                current.previous.next = current.next
                if current.next:
                    current.next.previous = current.previous
                break
            current = current.next


if __name__ == "__main__":
    lyst = TwoWayNode()
    lyst.add(1)
    lyst.add(2)
    lyst.append(3)
    lyst.append(3)
    lyst.append(3)
    lyst.append(3)
    lyst.append(3)
    lyst.append(4)
    lyst.traversal()
    lyst.traversal(beginning="tail")
    lyst.insert(1, 5)
    lyst.traversal()
    lyst.traversal(beginning="tail")
    print(lyst.search(3))
    print(lyst.search(6))
    lyst.remove(3)
    lyst.traversal()
    lyst.remove(1)
    lyst.traversal()
    lyst.remove(5)
    lyst.traversal()