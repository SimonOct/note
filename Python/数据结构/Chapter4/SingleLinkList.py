class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class SingleLinkList(object):

    def __init__(self, node=None):
        if node is None:
            self.__head = node
        else:
            head_node = Node(node)
            self.__head = head_node

    def is_empty(self) -> bool:
        return self.__head is None

    def length(self) -> int:
        count = 0
        current = self.__head
        # 需要将所有元素都取出来或者计算一次,则用cur is not None,需要定位到最后一个元素则用cur.next is not None
        while current is not None:
            count += 1
            current = current.next
        return int(count)

    def travel(self):
        current = self.__head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print("\n")

    def add(self, item):
        """在头部添加节点"""
        # 先把节点创建出来，记作node
        node = Node(item)
        # 将node链接域(next)指向头节点
        node.next = self.__head
        # 将链表的头重新指向新添加的节点
        self.__head = node

    def append(self, item):
        """追加节点"""
        node = Node(item)
        current = self.__head
        # 如果链表为空,直接追加
        if self.is_empty():
            self.__head = node
        else:
            # 将cur指向最后的节点,然后将其next指向node
            while current.next is not None:
                current = current.next
            current.next = node

    def insert(self, position: int, item):
        """在指定位置中添加元素"""
        if position <= 0:
            self.add(item)
        elif position > (self.length() - 1):
            self.append(item)
        else:
            count = 0
            node = Node(item)
            current = self.__head
            # 让cur指向position的前一个位置
            while count < (position - 1):
                count += 1
                current = current.next
            # 将node的next指向cur的next
            node.next = current.next
            # 将cur的next指向node
            current.next = node

    def remove(self, item):
        previous = None
        current = self.__head
        while current is not None:
            # 如果能找到匹配的
            if current.data == item:
                # 如果要删除的节点在开头
                if not previous:
                    self.__head = current.next
                else:
                    previous.next = current.next
                # 跳出while循环
                break
            else:
                previous = current
                current = current.next

    def search(self, item):
        current = self.__head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False


if __name__ == "__main__":
    lyst = SingleLinkList()
    print(lyst.is_empty())
    print(lyst.length())

    lyst.append(1)
    print(lyst.is_empty())
    print(lyst.length())

    lyst.append(2)
    lyst.append(3)
    lyst.append(4)
    lyst.append(5)
    lyst.append(6)
    lyst.travel()

    lyst.insert(5, 400)
    lyst.travel()

    lyst.remove(400)
    lyst.travel()

    lyst.remove(1)
    lyst.travel()
