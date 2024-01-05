# //Using array to understand the solution
class MyHashMap {
public:
    int data[1000001];
    MyHashMap() {
        fill(data, data + 1000000, -1);
    }
    void put(int key, int val) {
        data[key] = val;
    }
    int get(int key) {
        return data[key];
    }
    void remove(int key) {
        data[key] = -1;
    }
};



REAL SOLUTION :

class Node:
    def __init__(self, k, v, n):
        self.key = k
        self.val = v
        self.next = n

class MyHashMap:
    size = 19997
    mult = 12582917

    def __init__(self):
        self.data = [None] * self.size

    def hash(self, key):
        return int((key * self.mult) % self.size)

    def put(self, key, val):
        self.remove(key)
        h = self.hash(key)
        node = Node(key, val, self.data[h])
        self.data[h] = node

    def get(self, key):
        h = self.hash(key)
        node = self.data[h]
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return -1

    def remove(self, key):
        h = self.hash(key)
        node = self.data[h]
        if not node:
            return
        if node.key == key:
            self.data[h] = node.next
            del node
        else:
            while node.next:
                if node.next.key == key:
                    temp = node.next
                    node.next = temp.next
                    del temp
                    return
                node = node.next


# TIME COMPLEXITY :-
# hash function: O(1) time complexity, as it simply performs some arithmetic operations on the input key to compute an index in the array.

# put method: O(1) time complexity on average case, but could be O(n) in the worst case. In the average case, the key-value pair is added to the linked list at the computed index, which takes constant time. 
#     In the worst case, however, there could be n elements in the linked list at the computed index, where n is the number of key-value pairs in the hashmap. 
#     In this case, the remove method would be called first, which has a time complexity of O(n) in the worst case due to the need to iterate over the linked list to find the node with the key. 
#     Then, a new node would need to be created and added to the start of the linked list, which also takes O(n) time in the worst case since all the nodes in the linked list need to be shifted down by one to make room for the new node.

# get method: O(1) time complexity on average case, but could be O(n) in the worst case. In the average case, the value associated with the input key is found in constant time since the linked list at the computed index is expected to be small.
#     In the worst case, however, there could be n elements in the linked list at the computed index, where n is the number of key-value pairs in the hashmap. 
#         In this case, the for loop needs to iterate over all n nodes in the linked list to find the node with the input key, which takes O(n) time.

# remove method: O(1) time complexity on average case, but could be O(n) in the worst case. In the average case, the node with the input key is found and removed from the linked list at the computed index in constant time.
#     In the worst case, however, there could be n elements in the linked list at the computed index, where n is the number of key-value pairs in the hashmap. 
#     In this case, the for loop needs to iterate over all n nodes in the linked list to find the node with the input key, which takes O(n) time. 
#     Once the node is found, it takes constant time to delete it from the linked list.
