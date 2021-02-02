import queue


class Node:
    def __init__(self, value=None):
        self.value = value


class BinarySearchTree:

    # deque will be in use inside BFS method
    def __init__(self):
        self.q = queue.Queue()

    def __repr__(self):
        return str(self.q.queue)

    def push(self, value):
        self.q.put(value)

    def pop(self):
        self.q.get()

    def get_head(self):
        pass


# Test
b = BinarySearchTree()
b.push(1)
b.push(2)
b.push(3)
b.push(4)
b.push(5)
b.push(6)
print(b)
print(b.q.get())
print('******** pop ************')
b.pop()
print(b)
b.pop()
print(b)
b.pop()
print(b)
b.pop()
print(b)
b.pop()
print(b)
b.pop()
print(b)
b.pop()
print(b)
b.pop()
b.pop()
b.pop()
b.pop()
b.pop()
b.pop()
b.pop()

# print(b.q.empty())
print(b)
