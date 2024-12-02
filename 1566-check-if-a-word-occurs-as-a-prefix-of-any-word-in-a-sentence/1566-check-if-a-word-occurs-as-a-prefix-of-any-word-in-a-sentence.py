class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        s=sentence.split(' ')
        for index,word in enumerate(s):
            if len(word)>=len(searchWord):
                if word[:len(searchWord)]==searchWord:
                    return index+1
        return -1