class TrieNode:

    def __init__(self):
        self.node_list = [None]*26
        self.complete_word = False    

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        if word == None or len(word)==0:
            return
        i = 0
        while i < len(word):
            if not node.node_list[ord(word[i]) - ord('a')]:
                child_node = TrieNode()
                node.node_list[ord(word[i]) - ord('a')] = child_node
                node = child_node
            else:
                node = node.node_list[ord(word[i]) - ord('a')]
            i += 1
        node.complete_word = True

        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        if word == None or len(word) == 0:
            return False
        i = 0
        while i<len(word):
            node_ch = node.node_list[ord(word[i]) - ord('a')]
            if node_ch:
                node = node_ch
                i += 1
            else:
                return False
        return node.complete_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        if prefix == None or len(prefix) == 0:
            return False
        i = 0

        while i<len(prefix):
            node_ch = node.node_list[ord(prefix[i]) - ord('a')]
            if node_ch:
                node = node_ch
                i += 1
            else:
                return False
        return True          
        


trie = Trie()

print(trie.insert("apple"))
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("a"))
print(trie.insert("app"))
print(trie.search("app"))

trie = Trie()
print(trie.root.node_list)
print(trie.startsWith("a"))