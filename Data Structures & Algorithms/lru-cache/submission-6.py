class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            currNode = self.cache[key]

            currNode.next.prev = currNode.prev
            currNode.prev.next = currNode.next
            currNode.next = self.tail
            currNode.prev = self.tail.prev
            currNode.prev.next = currNode
            self.tail.prev = currNode

            return currNode.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            updateNode = self.cache[key]
            updateNode.val = value

            updateNode.next.prev = updateNode.prev
            updateNode.prev.next = updateNode.next
            updateNode.next = self.tail
            updateNode.prev = self.tail.prev
            updateNode.prev.next = updateNode
            self.tail.prev = updateNode
        else:
            newNode = Node(key, value)

            tmp = self.tail.prev
            newNode.next = self.tail
            self.tail.prev = newNode
            tmp.next = newNode
            newNode.prev = tmp

            self.cache[key] = newNode
            if len(self.cache) > self.capacity:
                removeKey = self.head.next.key
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
                del self.cache[removeKey]
