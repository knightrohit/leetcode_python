import collections
from functools import reduce

class Solution(object):
    def replaceWords(self, roots, sentence):
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        #print("Trie", trie, Trie, collections.defaultdict(dict))
        END = True

        for root in roots:
            #print(reduce(dict.__getitem__, root, trie)[])
            reduce(dict.__getitem__, root, trie)[END] = root
        print(trie)
        def replace(word):
            cur = trie
            for letter in word:
                if letter not in cur or END in cur: break
                cur = cur[letter]
            return cur.get(END, word)

        return " ".join(map(replace, sentence.split()))



sentence = "the cattle was rattled by the battery"

s_obj = Solution()
s_obj.replaceWords(["cat", "bat", "rat"], sentence)