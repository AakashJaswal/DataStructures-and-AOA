class TrieNode:
    def __init__(self):
        self.neighbours = {}
        self.word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.neighbours:
                curr.neighbours[ch] = TrieNode()
            curr = curr.neighbours[ch]
        curr.word = True

    def search(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.neighbours:
                return False
            curr = curr.neighbours[ch]
        return curr.word

    def startWith(self, prefix):
        curr = self.root
        for ch in prefix:
            if ch not in curr.neighbours:
                return False
            curr = curr.neighbours[ch]
        return True


TR = Trie()
TR.insert("apple")
TR.insert("bike")

print(TR.search("aap"))
print(TR.search("apple"))
print(TR.startWith("ap"))
