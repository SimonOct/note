
from arrays import Array
from node import Node

a = Array(6)
for i in range(0, 6):
    a[i] = i
print(a)

b = None
for i in range(0, len(a)):
    b = Node(a[i], b)

while b != None:
    print(b.data)
    b = b.next