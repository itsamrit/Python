class Node:
    def __init__(self):
        self.m = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.node = Node()

    def insert(self, word):
        root = self.node
        for i in range(len(word)):
            if not word[i] in root.m:
                root.m[word[i]]= Node()
            root = root.m[word[i]]
        root.is_end = True
    
    def search(self, word):
        root = self.node
        for i in range(len(word)):
            if not word[i] in root.m:
                return False
            root = root.m[word[i]]
        if root.is_end == True:
            return True
        return False
    
    def startsWith(self, word):
        root = self.node
        for i in range(len(word)):
            if not word[i] in root.m:
                return False
            root = root.m[word[i]]
        
        return True


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app")) 
print(trie.startsWith("app")) 
trie.insert("app")
print(trie.search("app")) 
