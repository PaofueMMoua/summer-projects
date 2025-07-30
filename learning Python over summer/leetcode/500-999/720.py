class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()

        # populate all the elements in the trie
        # word by word, no need for sorting here
        for word in words:
            cur = root
            for letter in word:
                if letter not in cur.children:
                    cur.children[letter] = TrieNode()
                cur = cur.children[letter]
            cur.end = True
            
        res = ''
        
        # iterate over all the words
        # in our words array
        for word in words:
            # if the length of the word
            # isn't > our res, there's no
            # point in exploring further
            # since we want the longest word
            if len(word) < len(res): continue
            
            # start a temp cur var
            # init at root to iterate
            # trie for every word
            cur = root
            
            # for every letter in the current
            # word, traverse the trie and see
            # that for every letter in this
            # word, there's a node in the trie
            # which has end = True (i.e. a word 
            # on its own, if not just break out)
            for letter in word:
                cur = cur.children[letter]
                if not cur.end: break
            
            # proceed only if you didn't break
            # out of the previous loop (cur.end == True)
            # and then check if the cur word is longer
            # than the cur res, or if they are equal in length
            # use the lexicographically smaller one (word < res)
            if cur.end and (len(word) > len(res) or (len(word) == len(res) and word < res)):
                res = word        
            
        return res