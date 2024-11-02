class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words=sentence.split(' ')
        first_word,last_word=words[0],words[-1]
        if last_word[-1]!=first_word[0]:
            return False
        for i in range(1,len(words)):
            prev=words[i-1][-1]
            current=words[i][0]
            if prev!=current:
                return False
        return True