class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])

        words = normalized_str.split()
        print(words)
        word_count = {}

        for word in words:
            if word not in banned:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

        max_freq = max(word_count.values())
        for k, v in word_count.items():
            if v == max_freq:
                return k

        

