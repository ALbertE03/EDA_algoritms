class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.back = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        self.size += 1
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.back = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def appendleft(self, data):
        self.size += 1
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.back = new_node
            self.head = new_node

    def pop(self):
        if not self.tail:
            raise "no hay elementos"
        data = self.tail.data
        self.tail = self.tail.back
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self.size -= 1
        return data

    def popleft(self):
        if not self.head:
            raise "no hay elementos"
        data = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.back = None
        else:
            self.tail = None
        self.size -= 1
        return data

    def __str__(self):
        result = "["
        actual = self.head
        while actual:
            result += str(actual.data)
            actual = actual.next
            if actual:
                result += ", "
        result += "]"
        return result


d = Deque()
d.append(1)
d.append(2)
d.appendleft(0)
d.append(22)
d.appendleft(12)
print(d)
print(d.size)
print(d.popleft())
print(d)
print(d.size)
print(d.pop())
print(d.popleft())
print(d)
print(d.size)
