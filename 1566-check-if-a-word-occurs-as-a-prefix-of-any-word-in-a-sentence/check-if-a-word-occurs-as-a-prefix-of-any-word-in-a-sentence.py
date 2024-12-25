class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(' ')
        j = 0
        k = 0 #add k here

        while j < len(searchWord) and k < len(words): #add k condition
            i = 0 #reset i for every word
            while i < len(words[k]) and j < len(searchWord): #add j condition
                if words[k][i] == searchWord[j]:
                    j += 1
                    i += 1 #add i increment
                else:
                    break #break out of inner loop if no match
            if j == len(searchWord):
                return k + 1
            j=0 #reset j for the next word
            k+=1 #increment k

        return -1