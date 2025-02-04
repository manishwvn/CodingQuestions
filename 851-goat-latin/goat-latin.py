class Solution:
    def toGoatLatin(self, sentence: str) -> str:

        words = sentence.split()
        result = []

        for i in range(len(words)):
            word = words[i]
            res_word = ""
            
            if word[0].lower() in {'a', 'e', 'i', 'o', 'u'}:
                res_word += word + "ma"

            else:
                res_word += word[1:] + word[0] + "ma"

            res_word += ('a' * (i+1))
            result.append(res_word)
        
        return " ".join(result)


        