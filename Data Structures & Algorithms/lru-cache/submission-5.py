from collections import defaultdict
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        try:
            currNode = self.cache[key]
            currNode.prev.next = currNode.next
            currNode.next.prev = currNode.prev

            currNode.prev = self.tail.prev
            currNode.next = self.tail
            self.tail.prev.next = currNode
            self.tail.prev = currNode

            return currNode.val
        except:
            return -1

    def put(self, key: int, value: int) -> None:
        newNode = None
        try:
            newNode = self.cache[key]
            newNode.val = value

            newNode.prev.next = newNode.next
            newNode.next.prev = newNode.prev
        except:
            newNode = Node(key,value)
            self.cache[key] = newNode

        newNode.prev = self.tail.prev
        newNode.next = self.tail
        self.tail.prev.next = newNode
        self.tail.prev = newNode

        if len(self.cache) > self.capacity:
            self.cache.pop(self.head.next.key)
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
            
        
