class TrieNode:
    def __init__(self):
        self.children = {}
        self.wordEnd = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.wordEnd = True

    def search(self, word: str) -> bool:
        node = self.root

        def backtrack(node, index):
            if index == len(word):
                return node.wordEnd
            
            currentChar = word[index]
            # backtrack
            if currentChar == '.':
                for children in node.children.values():
                    if backtrack(children, index + 1):
                        return True
                return False
            else:
                if currentChar not in node.children:
                    return False
                return backtrack(node.children[currentChar], index + 1)
        
        return backtrack(node, 0)
        
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)