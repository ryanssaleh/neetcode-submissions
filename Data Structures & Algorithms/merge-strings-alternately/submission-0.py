class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i1 = 0
        i2 = 0
        alt_str = ''
        while not (i1 >= len(word1) or i2 >= len(word2)):
            alt_str += word1[i1]
            alt_str += word2[i2]
            i1, i2 = i1 + 1, i2 + 1
        
        assert i1 == len(word1) or i2 == len(word2)

        if i1 == len(word1):
            alt_str += word2[i2:]
        else:
            alt_str += word1[i1:]
        return alt_str
        