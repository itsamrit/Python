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




//LFU CACHE HARD

class LFUCache {
    unordered_map<int,pair<int,int>> cache; // map[key] = {value,count}
    vector<deque<int>> counter; // one deque per count
    int max_size, num_elements;

    void increment_element(int key) {
        // increment cache counter
        cache[key].second++;
        // increase size of counter if necessary
        while (counter.size() <= cache[key].second)
            counter.push_back(deque<int>());
        // add a new element into the appropriate deque
        counter[cache[key].second].push_back(key);
    }

    void remove_LFU_element() {
        bool success = false;
        // start from the front of the counter
        for (int i = 0; i < counter.size() && !success; i++) {
            // start at the front of each deque
            while (!counter[i].empty() && !success) {
                // if this count is valid, delete the entry in the cache
                if (cache[counter[i].front()].second == i) {
                    success = true;
                    cache.erase(counter[i].front());
                    num_elements--;
                }
                counter[i].pop_front(); // delete invalid and 1st valid
            }
        }
    }

public:
    LFUCache(int c) {
        max_size = c;
        num_elements = 0;
        counter = {{}};
    }

    int get(int key) {
        // if not found, return -1
        if (cache.find(key) == cache.end())
            return -1;
        // count use
        increment_element(key);
        // return the value
        return cache[key].first;
    }
    
    void put(int key, int value) {
        // protect against capacity = 0
        if (max_size == 0) return;
        // if key exists
        if (cache.find(key) != cache.end()) {
            cache[key].first = value;
            increment_element(key);
            return;
        }
        // if at capacity
        if (num_elements == max_size)
            remove_LFU_element();
        // add the new key
        cache[key] = make_pair(value,0);
        counter[0].push_back(key);
        num_elements++;
    }
};
