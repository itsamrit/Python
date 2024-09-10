// LRU put() function removes least recently used if capacity to put new node is full & puts the new node
// get() & put() function makes the node most recently used .both have tc o(1)
// if something already exist remove the previous key,value of it & insert or put new node, no removal of lru needed even if capacity is full since we are removing 1 node

# 🐍Python does not have explicit pointers like C++, so the linked list operations are performed using the actual objects. Additionally, Python automatically handles memory management, so there's no need for explicit memory deallocation.
//🟩Modified DOUBLY LINKEDLIST which stores 2 values instead of 1 since we need to store key-value pair

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

    #IMPLEMENTATION USING DICT
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        #Time Complexity: O(1)
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        #Time Complexity: O(1)
        if key not in self.cache:
            return -1 
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        #Time Complexity: O(1)
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        # If the cache exceeds its capacity, remove the least recently used item.
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# IMPLEMENTATION USING LINKEDLIST
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

from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_val = defaultdict(lambda: None)  # Stores key-value pairs with default None
        self.key_to_freq = defaultdict(int)  # Stores key-frequency pairs with default 0
        self.freq_to_keys = defaultdict(OrderedDict)  # Maps frequency to an ordered dict of keys

    def update(self, key):
        #Time Complexity: O(1) amortized
        freq = self.key_to_freq[key]
        val = self.key_to_val[key]

        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if freq == self.min_freq:
                self.min_freq += 1

        # Add the key to the new frequency list
        self.key_to_freq[key] = freq + 1
        self.freq_to_keys[freq + 1][key] = val

    def get(self, key) :
        #Time Complexity: O(1) amortized
        if key not in self.key_to_val or self.key_to_val[key] is None:
            return -1
        
        self.update(key)
        return self.key_to_val[key]

    def put(self, key, value):
        # Time Complexity: O(1) amortized
        if self.capacity == 0:
            return

        if key in self.key_to_val and self.key_to_val[key] is not None:
            self.key_to_val[key] = value
            self.update(key)
        else:
            if len(self.key_to_val) == self.capacity:
                evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
                del self.key_to_val[evict_key]
                del self.key_to_freq[evict_key]

            # Insert the new key-value pair
            self.key_to_val[key] = value
            self.key_to_freq[key] = 1
            self.freq_to_keys[1][key] = value
            self.min_freq = 1
