from node import Node


class LinkedBag(object):

    def __init__(self, sourceCollection=None):
        self.items = None
        self.size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def __iter__(self):
        cursor = self.items
        while cursor is not None:
            yield cursor.data
            cursor = cursor.next

    def clear(self):
        """Makes self become empty."""
        self.size = 0
        self.items = None

    def add(self, item):
        self.items = Node(item, self.items)
        self.size += 1

    def remove(self, item):
        if item not in self:
            raise KeyError(str(item) + "not in bag")
        probe = self.items
        trailer = None
        for trageItem in self:
            if trageItem == item:
                break
            trailer = probe
            probe = probe.next
        if probe == self.items:
            self.items = self.items.next
        else:
            trailer.next = probe.next
        self.size -= 1

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return self.size

    def __str__(self):
        return "{" + ", ".join(map(str, self)) + "}"

    def __add__(self, other):
        result = LinkedBag(self)
        for item in other:
            result.add = Node(item)
        return result

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) != type(other) or \
                len(self) != len(other):
            return False
        for item in self:
            if item not in other:
                return False
        return True


