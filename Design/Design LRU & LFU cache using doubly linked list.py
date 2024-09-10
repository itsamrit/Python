// LRU put() function removes least recently used if capacity to put new node is full & puts the new node
// get() & put() function makes the node most recently used .both have tc o(1)
// if something already exist remove the previous key,value of it & insert or put new node, no removal of lru needed even if capacity is full since we are removing 1 node

# 🐍Python does not have explicit pointers like C++, so the linked list operations are performed using the actual objects. Additionally, Python automatically handles memory management, so there's no need for explicit memory deallocation.
//🟩Modified DOUBLY LINKEDLIST which stores 2 values instead of 1 since we need to store key-value pair

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
class LRUCache:
    class Node:
        def __init__(self, k, v):
            self.key = k
            self.val = v
            self.prev = None
            self.next = None

    def __init__(self, cap):
        self.capacity = cap
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.m = {}

    def deleteNode(self, curNode):
        prevNode = curNode.prev
        nextNode = curNode.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def addNode(self, curNode):
        curNode.next = self.head.next
        curNode.prev = self.head
        curNode.next.prev = curNode
        self.head.next = curNode

    def get(self, key):
        if key not in self.m:
            return -1
        curNode = self.m[key]
        result = curNode.val
        del self.m[key]
        self.deleteNode(curNode)
        self.addNode(curNode)
        self.m[key] = self.head.next
        return result

    def put(self, key, value):
        if key in self.m:
            curNode = self.m[key]
            del self.m[key]
            self.deleteNode(curNode)

        if len(self.m) == self.capacity:
            del self.m[self.tail.prev.key]
            self.deleteNode(self.tail.prev)

        self.addNode(self.Node(key, value))
        self.m[key] = self.head.next




#LFU CACHE HARD

from collections import deque, defaultdict

class LFUCache:
    def __init__(self, capacity):
        self.cache = {}  # {key: (value, count)}
        self.counter = [deque()]  # list of deques, one deque per count
        self.max_size = capacity
        self.num_elements = 0

    def increment_element(self, key):
        value, count = self.cache[key]
        self.cache[key] = (value, count + 1)
        
        # Extend the counter list if needed
        while len(self.counter) <= count + 1:
            self.counter.append(deque())
        
        # Add the key to the new deque corresponding to the incremented count
        self.counter[count + 1].append(key)

    def remove_LFU_element(self):
        success = False
        
        # Iterate over deques in the counter list, starting from the least count
        for i in range(len(self.counter)):
            while self.counter[i] and not success:
                key = self.counter[i][0]  # Front of the deque
                
                # Only remove if count matches
                if self.cache[key][1] == i:
                    success = True
                    self.cache.pop(key)  # Remove the element from the cache
                    self.num_elements -= 1
                # Remove the element from the deque (whether valid or invalid)
                self.counter[i].popleft()
                
            if success:
                break

    def get(self, key):
        if key not in self.cache:
            return -1
        self.increment_element(key)
        return self.cache[key][0]

    def put(self, key, value):
        # If the cache capacity is 0, do nothing
        if self.max_size == 0:
            return
        
        # If the key is already in the cache, update the value and increment usage
        if key in self.cache:
            self.cache[key] = (value, self.cache[key][1])
            self.increment_element(key)
            return
        
        # If the cache is full, remove the least frequently used element
        if self.num_elements == self.max_size:
            self.remove_LFU_element()
        
        # Add the new key with value and count of 0
        self.cache[key] = (value, 0)
        self.counter[0].append(key)
        self.num_elements += 1
