class TrieNode:
    def __init__(self):
        self.child = dict()
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.child:
                node.child[char] = TrieNode()
            node = node.child[char]
        node.count += 1

    def query(self, pattern):
        node = self.root
        for char in pattern:
            if char == '*':
                break
            if char in node.child:
                node = node.child[char]
            else:
                return 0
        return self.findAll(node)
    
    def findAll(self, node):
        count = node.count
        for char in node.child:
            count += self.findAll(node.child[char])
        return count


def solve():
    N, Q = map(int,input().split())
    forward_trie = Trie()
    reverse_trie = Trie()
    for _ in range(N):
        word = input().strip()
        forward_trie.insert(word)
        reverse_trie.insert(word[::-1])
    for _ in range(Q):
        pattern = input().strip()
        if pattern[0] == '*':
            print(reverse_trie.query(pattern[::-1]))
        else:
            print(forward_trie.query(pattern))

solve()