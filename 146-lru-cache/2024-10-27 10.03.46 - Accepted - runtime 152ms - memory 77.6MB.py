class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next, self.prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyMap = {}
        self.tail, self.head = Node(0, 0), Node(0, 0)
        self.tail.next, self.head.prev = self.head, self.tail
    
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        node.prev, node.next = None, None
    
    def insert(self, node):
        prev = self.head.prev
        prev.next = self.head.prev = node
        node.prev, node.next = prev, self.head

    def get(self, key: int) -> int:
        if key in self.keyMap:
            # move the node to the front of the ll, return value
            node = self.keyMap[key]
            self.remove(node)
            self.insert(node)
            return node.value
        else:
            return -1
            

    def put(self, key: int, value: int) -> None:
        if key in self.keyMap:
            self.remove(self.keyMap[key])
        node = Node(key, value)
        self.insert(node)
        self.keyMap[key] = node

        if len(self.keyMap.keys()) > self.capacity:
            del self.keyMap[self.tail.next.key]
            self.remove(self.tail.next)
         
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)