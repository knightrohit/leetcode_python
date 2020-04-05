from collections import defaultdict
from functools import reduce

class TrieSentence:
    def __init__(self):
        trie = lambda:defaultdict(trie)
        self.trie_dict = trie()
        self.count = 0

class AutocompleteSystem:

    def __init__(self, sentences, times):
        self.input_ch = []
        self.root = TrieSentence()
        for sent, count in zip(sentences, times):
            reduce(dict.__getitem__, sent, self.root.trie_dict)['count'] = count
                
    def input(self, c):
        self.input_ch.append(c)
        sent_dict = {}
        sent = []
        trie = self.root
        for ch in self.input_ch:
            if ch in trie.trie_dict:
                new_ch = ch
                while trie.trie_dict:
                    new_ch = trie.trie_dict[new_ch]
                    sent.append(new_ch)
                    if 'count' in trie.trie_dict:
                        sent_dict[''.join(sent)] = trie.trie_dict[count]
                    trie = trie.trie_dict[new_ch]
                    print(trie)
        print(sent)  
        #sort 
        out = []
        prev_count = 0
        prev_sent  = None
        i = 0
        for val, sent in sorted(sent_dict.items(), key = lambda x: x[1], reverse = True):
            if prev_count:
                if prev_count > val:
                    out.append(prev_sent)
                elif prev_count == val:
                    for i in range(min(len(prev_sent), len(v))):
                        if ord(prev_sent[i]) < ord(sent[i]):
                            prev_sent = sent
                            prev_count = val
                            break
                    if sent != prev_sent:
                        if len(sent) > len(prev_sent):
                            prev_sent = sent
                            prev_count = val      
                            
                    
            else:
                prev_sent = sent
                prev_count = val
                
        return out   
        
        
        
        


obj = AutocompleteSystem(["i love you","island","iroman","i love leetcode"],[5,3,2,2])
#print(obj.root.trie_dict)
param_1 = obj.input('i')
print(param_1)